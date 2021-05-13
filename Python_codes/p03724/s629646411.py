import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    count = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        count[a] += 1
        count[b] += 1

    if all(c % 2 == 0 for c in count):
        ans = "YES"
    else:
        ans = "NO"
    print(ans)


if __name__ == "__main__":
    main()
