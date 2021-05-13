import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, A, B = map(int, input().split())

ans = 0
for i in range(1, N+1):
    sum_ = sum(map(int, list(str(i))))
    if A <= sum_ <= B:
        ans += i
print(ans)