import sys

N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().rsplit()))
mod = 10 ** 9 + 7

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            cnt += 1
res = (K * cnt) % mod
cnt2 = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            cnt2 += 1
    for j in range(i + 1, N):
        if A[i] > A[j]:
            cnt2 += 1
res += (cnt2 * ((K * (K - 1)) // 2)) % mod
print(res % mod)