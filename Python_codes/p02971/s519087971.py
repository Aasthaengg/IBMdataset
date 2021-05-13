import sys
from collections import Counter


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = [int(input()) for _ in range(n)]
    cnt = Counter(a)
    maximum = max(a)
    if cnt[maximum] > 1:
        print("\n".join([str(maximum)] * n))
    else:
        second = sorted(a, reverse=True)[1]
        for i in range(n):
            if a[i] != maximum:
                print(maximum)
            else:
                print(second)


if __name__ == "__main__":
    main()
