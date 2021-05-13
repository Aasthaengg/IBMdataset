mod=10**9+7
k=int(input())
s=input()
l=len(s)
fact=[1]
for i in range(1,k+l+1):
  fact.append((fact[-1]*i)%mod)
revfact=[]
for i in range(k+l+1):
  revfact.append(pow(fact[i],mod-2,mod))
pows1=[1]
pows2=[1]
for i in range(1,k+l+1):
  pows1.append((pows1[-1]*25)%mod)
  pows2.append((pows2[-1]*26)%mod)
ans=0
for i in range(l,l+k):
  ans+=pows2[l+k-i-1]*fact[i]*revfact[i-l]*revfact[l]*pows1[i-l]
  ans%=mod
ans+=fact[l+k]*revfact[k]*revfact[l]*pows1[k]
ans%=mod
print(ans)