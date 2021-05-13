N,M = map(int,input().split())
digit = 'zero padding: {:0=6}'
dic = [[] for _ in range(N+1)]

for i in range(M):
    p,y = map(int,input().split())
    dic[p].append((y,i))

for p in dic:
    p.sort()

ans = [None for _ in range(M)]
for k in range(1,N+1):
    p = dic[k]
    for j in range(len(p)):
        i = p[j][1]
        ID = str(k).zfill(6)+str(j+1).zfill(6)
        ans[i] = ID

for a in ans:
    print(a)
