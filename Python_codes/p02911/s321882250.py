import sys
from collections import Counter


def main():
    input = sys.stdin.buffer.readline
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    cnt = Counter(a)
    for i in range(1, n + 1):
        print("Yes" if q - cnt[i] < k else "No")


if __name__ == "__main__":
    main()
