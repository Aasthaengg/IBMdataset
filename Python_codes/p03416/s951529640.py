import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

A, B = map(int, input().split())

ans = 0
for i in range(A, B+1):
    if str(i) == str(i)[::-1]:
        ans += 1
print(ans)