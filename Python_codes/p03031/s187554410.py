from itertools import product

#入力
N,M=map(int,input().split())
ks=[list(map(int,input().split())) for _ in range(M)]
p=[int(x) for x in input().split()]
#print(ks)

ans=0
for i in product([0,1],repeat=N):
    ok=True
    for j in range(M):
        j_on_cnt=0
        for k in ks[j][1:]:
            j_on_cnt+=i[k-1]
            
        if j_on_cnt%2 != p[j]:
            ok=False
            break
    if ok:
        ans+=1
print(ans)