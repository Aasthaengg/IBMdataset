N,T=map(int,input().split())
t=[int(i) for i in input().split()]+[10**15]
ans=0
for i in range(N):
    ans+=min(t[i+1]-t[i],T)
print(ans)
