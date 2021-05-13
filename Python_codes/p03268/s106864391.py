import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, read().split())
memo = (n // k) ** 3
if k % 2 == 0:
    memo += ((n + k // 2) // k) ** 3
print(memo)
