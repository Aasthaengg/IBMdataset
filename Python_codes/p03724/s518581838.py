import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    cnt = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b] += 1

    ans = "YES" if all(c % 2 == 0 for c in cnt) else "NO"
    print(ans)


if __name__ == "__main__":
    main()
