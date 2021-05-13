import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = int(input().strip())
    A = [int(i) for i in input().strip().split()]
    odds = 1
    for a in A:
        if a % 2 == 0:
            odds *= 2
        else:
            continue

    return 3**N - odds


if __name__ == "__main__":
    print(main())