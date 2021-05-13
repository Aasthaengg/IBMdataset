inf = float('inf')

N, T = map(int, input().split())
A = list(map(int, input().split()))

cm = [inf] * N
m = inf
for i, a in enumerate(A):
    m = min(m, a)
    cm[i] = m

cM = [-inf] * N
M = -inf
for i, a in enumerate(A[::-1]):
    M = max(M, a)
    cM[i] = M
cM.reverse()

diff = 0
for m, M in zip(cm, cM):
    diff = max(diff, M - m)

ans = 0
for a, M in zip(A, cM):
    if a + diff <= M:
        ans += 1
print(ans)