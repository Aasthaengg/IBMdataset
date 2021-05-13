from itertools import product
N, *P = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
res = []
for p in product((0,1,2,3),repeat=N):
    tmp = [0]*4
    cnt = [0]*4
    for i in range(N):
        tmp[p[i]] += L[i]
        cnt[p[i]] += 1
    if cnt[1]>=1 and cnt[2]>=1 and cnt[3]>=1:
        res.append(sum(abs(tmp[i]-P[i-1]) + (cnt[i]-1)*10 for i in range(1,4)))
print(min(res))