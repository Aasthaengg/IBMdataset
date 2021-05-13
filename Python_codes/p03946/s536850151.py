N,T = map(int, input().split())
A = [int(i) for i in input().split()]

# 買う数 == 売る数
if T % 2 == 1:
    T -= 1

from heapq import heappop,heappush

place = []
MINA = [float("inf")] * N
for i in range(N):
    if i == 0:
        MINA[i] = A[i]
    else:
        MINA[i] = min(MINA[i-1], A[i])

sub = []
for a,m in zip(A,MINA):
    heappush(sub, m - a)

ans = 1
MAXSUB = heappop(sub)
while sub:
    s = heappop(sub)
    if s == MAXSUB:
        ans += 1
    else:
        break

print(ans)