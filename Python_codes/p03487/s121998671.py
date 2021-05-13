import sys
from collections import Counter
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = int(input().strip())
    a_list = [int(n) for n in input().strip().split()]
    count = Counter(a_list)
    ans = 0
    for k, v in count.items():
        if v == k:
            continue
        elif v > k:
            ans += v - k
        else:
            ans += v
    return ans


if __name__ == '__main__':
    print(main())
