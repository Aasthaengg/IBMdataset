N=int(input())
K=int(input())
ans=1

i=1
while i<=N:
    if 2**(i-1)<=K:
        ans*=2
    else:
        ans+=K
    i+=1

print(ans)