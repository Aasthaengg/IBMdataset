import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())

res = 0
for k in range(1, N+1):
    y = N // k
    res += k * y * (y+1) // 2

print(res)