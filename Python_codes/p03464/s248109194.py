import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    K = int(input())
    A = read_list()[::-1]
    if A[0] != 2:
        print(-1)
        return

    minN = 2
    maxN = 2
    for a in A:
        minN = ((minN - 1) // a + 1) * a
        maxN = (maxN // a + 1) * a - 1
    if minN > maxN:
        print(-1)
    else:
        print(minN, maxN)


if __name__ == "__main__":
    main()
