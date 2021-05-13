import sys

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

MOD = 10 ** 9 + 7

N, K = map(int, readline().split())
A = list(map(int, readline().split()))

tento1 = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            tento1 += 1
tento2 = 0
for i in range(N):
    for j in range(0, N):
        if A[i] > A[j]:
            tento2 += 1

ans = K * tento1 + (K * (K - 1)) // 2 * tento2
ans = ans % MOD
print(ans)