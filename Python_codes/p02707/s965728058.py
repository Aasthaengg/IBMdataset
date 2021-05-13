import sys
from collections import Counter


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    for i in range(1, n + 1):
        print(cnt[i])


if __name__ == '__main__':
    main()
