import bisect
import itertools

N, M  = map(int,input().split())
A = sorted(list(map(int,input().split())))
D = []

for i in range(M):
    B, C = map(int,input().split())
    D.append((B,C))

D.sort(key = lambda x:x[1],reverse = True)

cnt = 0
ans = []
for b, c in D:
    for i in range(b):
        ans.append(c)
    cnt += b
    if cnt >=N:
        break
#print(D)
#print(ans)
res = sum(A)
for i in range(min(N,len(ans))):
    if ans[i]-A[i]>0:
        res += ans[i] - A[i]
    else:
        break
print(res)