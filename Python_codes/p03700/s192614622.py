import sys
from math import ceil
def input(): return sys.stdin.readline().strip()


def main():
    N, A, B = map(int, input().split())
    monster = [int(input()) for _ in range(N)]
    additional = A - B
    """
    Bの誘爆を基本に考えて決めうち二分探索を行う。
    """
    left = 0
    right = max(monster) // B + 1
    while right - left > 1:
        mid = (left + right) // 2
        times = 0
        for m in monster:
            times += max(0, ceil((m - B * mid) / additional))
        if times > mid:
            left = mid
        else:
            right = mid
    print(right)

if __name__ == "__main__":
    main()
