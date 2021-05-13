N,M = map(int,input().split())
l = list(map(int,input().split()))
S = sum(l)
c = 0
for i,k in enumerate(l):
    if k >= S/(4*M):
        c += 1
if c >= M:print('Yes')
else:print('No')