N=input()
N=int(N)

ans=0

for i in range(N):
    l,r=input().split()
    l=int(l)
    r=int(r)
    p=r-l+1
    ans+=p

print(ans)