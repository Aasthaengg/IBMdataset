import sys

input = sys.stdin.readline


def main():
    A, B, C, D = map(int, input().split())
    S1 = A * B
    S2 = C * D
    print(max(S1, S2))


if __name__ == "__main__":
    main()
