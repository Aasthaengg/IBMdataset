r=input().split()
N=int(r[0])
K=int(r[1])
d_pre=input().split()
d=[int(s) for s in d_pre]
d.sort()
ans=0
for i in range(K):
    ans+=d[i]
print(ans)