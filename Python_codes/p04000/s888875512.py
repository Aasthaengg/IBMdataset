import sys
from collections import defaultdict
input = sys.stdin.readline
H, W, N = map(int, input().split())

board = defaultdict(int)
black = []
for _ in range(N):
    a, b = map(int, input().split())
    black.append((a - 1, b - 1))
    board[(a-1) * W + (b - 1)] = 1

num = [0] * 10
for p in black:
    for ch in range(max(p[0] - 1, 1), min(p[0] + 2, H - 1)):
        for cw in range(max(p[1] - 1, 1), min(p[1] + 2, W - 1)):
            count = 0
            for h in range(ch - 1, ch + 2):
                for w in range(cw - 1, cw + 2):
                    if board[h * W + w] == 1:
                        count += 1
            num[count] += 1
for i in range(1, 10):
    num[i] //= i
print((H - 2) * (W - 2) - sum(num))
for i in range(1, 10):
    print(num[i])
