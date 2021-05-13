n=int(input())
s=input()
accum=[0]*n
if s[0]=="#":
    accum[0]=1
for i in range(n-1):
    accum[i+1]+=accum[i]+(s[i+1]=="#")
accum=[0]+accum
ans=10**18
for i in range(n+1):
    ans=min(ans,accum[i]+n-i-accum[n]+accum[i])
#print(accum)
print(ans)