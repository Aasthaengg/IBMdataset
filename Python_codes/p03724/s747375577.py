import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    cnt = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        cnt[a - 1] += 1
        cnt[b - 1] += 1

    ans = "YES"
    for c in cnt:
        if c % 2 != 0:
            ans = "NO"
    print(ans)


if __name__ == "__main__":
    main()
