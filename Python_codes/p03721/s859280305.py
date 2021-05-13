N,K=map(int,input().split())
C=[0]*(10**5+1)
for i in range(N):
    a,b=map(int,input().split())
    C[a]+=b
cnt=0
l=0
while cnt<K:
    l+=1
    cnt+=C[l]
print(l)
