import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()
    N = len(S)

    ans = 0
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
