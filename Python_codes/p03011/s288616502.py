import sys

input = sys.stdin.readline


def main():
    P, Q, R = map(int, input().split())
    ans = min(P + Q, Q + R, R + P)
    print(ans)


if __name__ == "__main__":
    main()
