from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def main():
    mod = 10**9 + 7
    n = int(input())
    colors = [int(input()) for _ in range(n)]
    pos_dict = {}
    for i, color in enumerate(colors):
        if color not in pos_dict:
            pos_dict[color] = deque([])
            continue
        pos_dict[color].append(i)

    branches = []
    base = 1
    for i, color in enumerate(colors):
        if branches and branches[0][0] == i:
            _, add = heappop(branches)
            base += add
            base %= mod

        if pos_dict[color]:
            next = pos_dict[color].popleft()
            if next == i+1:
                continue
            add = base
            heappush(branches, (next, add))

    print(base % mod)


if __name__ == "__main__":
    main()
