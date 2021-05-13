import sys

input = sys.stdin.readline


def main():
    N = int(input())
    x = y = 0
    for _ in range(N):
        A, B = map(int, input().split())
        if A > x:
            x = A
            y = B

    ans = x + y
    print(ans)


if __name__ == "__main__":
    main()
