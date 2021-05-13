import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')


N = int(input())
A = list(map(int, input().split()))


c = 1
ans = 0
for a in A:
    if a == c:
        c += 1
        continue
    ans += 1
if ans == N:
    print(-1)
else:
    print(ans)