import itertools
N,M=map(int,input().split())
s=[]
for _ in range(M):
    s.append(list(map(int,input().split()))[1:])
p=list(map(int,input().split()))
ans=0
for bit in itertools.product([0,1],repeat=N):
    count=[0]*M
    for light in range(M):
        for k in s[light]:
            count[light]+=bit[k-1]
    if all (count[i]%2==p[i] for i in range(M)):
        ans+=1
print(ans)