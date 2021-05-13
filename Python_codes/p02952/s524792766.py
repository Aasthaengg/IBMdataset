N=int(input())
ans=0
l=len(str(N))
for i in range(l+1):
    if i!=l and i%2!=0:
        ans+=(10**i)-(10**(i-1))
    if i==l and i%2!=0:
        ans+=(N-(10**(i-1))+1)
print(ans)