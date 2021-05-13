from collections import defaultdict as dd

N, M = map(int, input().split())
A = list(map(int, input().split()))

mods = dd(int)
mods[0] = 1

# 1-indexed
cuma = [0] * (N + 1)
for i in range(N):
    cuma[i + 1] = (cuma[i] + A[i]) % M

for i in range(N):
    mods[cuma[i + 1]] += 1

cnt = 0

for ci in set(cuma):
    m = mods[ci]
    cnt += m * (m - 1) // 2
print(cnt)
