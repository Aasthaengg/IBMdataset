import sys
from collections import Counter


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    comb = 0
    for v in cnt.values():
        if v >= 2:
            comb += v * (v - 1) // 2
    for k in range(n):
        if cnt[a[k]] >= 2:
            print(comb - (cnt[a[k]] - 1))
        else:
            print(comb)


if __name__ == "__main__":
    main()
