import sys

sys.setrecursionlimit(100000)
INF = float('inf')

K = int(sys.stdin.readline())

N = 50
ans = [a + K // N for a in range(N)]
for _ in range(K % N):
    min_a = min(ans)
    ans = [a + N if a == min_a else a - 1 for a in ans]
print(N)
print(*ans)
