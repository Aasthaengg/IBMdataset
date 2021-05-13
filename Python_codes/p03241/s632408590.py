N,M=map(int,input().split())
d=set()
k=1
while(k*k<=M):
    if M%k==0:
        d.add(k)
        d.add(M//k)
    k+=1
ans=1
for n in d:
    if n>=N:
        ans=max(ans,M//n)
print(ans)
