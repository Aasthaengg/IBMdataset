import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    P = []
    B = [True] * 56000
    for i in range(2, 55555):
        if B[i]:
            if i % 5 == 1:
                P.append(str(i))
            for j in range(56000 // i):
                B[i * j] = False
    print(" ".join(P[: int(input())]))


if __name__ == "__main__":
    main()
