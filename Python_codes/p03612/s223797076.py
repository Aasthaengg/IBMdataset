import sys

input = sys.stdin.readline


def main():
    N = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(N - 1):
        if p[i] == i + 1:
            ans += 1
            p[i], p[i + 1] = p[i + 1], p[i]
    if p[-1] == N:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
