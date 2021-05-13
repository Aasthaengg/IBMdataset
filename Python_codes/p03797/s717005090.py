import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, read().split())
if n * 2 < m:
    print(n + (m - n * 2) // 4)
else:
    print(m // 2)
