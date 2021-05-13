import sys

input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    if A == B == C and A % 2 == 0:
        print(-1)
        exit()

    ans = 0
    while True:
        if (A % 2 == 1) or (B % 2 == 1) or (C % 2 == 1):
            break
        ans += 1
        A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2

    print(ans)


if __name__ == "__main__":
    main()
