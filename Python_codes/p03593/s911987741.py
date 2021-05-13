import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W = map(int, input().split())
    count = Counter()
    for _ in range(H):
        count += Counter(input())

    four = (H // 2) * (W // 2)
    two = (H // 2) * (W % 2) + (W // 2) * (H % 2)
    one = (H % 2) * (W % 2)

    for value in count.values():
        while value >= 4 and four > 0:
            value -= 4
            four -= 1
        while value >= 2 and two > 0:
            value -= 2
            two -= 1
        while value >= 1 and one > 0:
            value -= 1
            one -= 1

    if four == two == one == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
