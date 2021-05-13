n=int(input())
s1=input()
s2=input()
mod=10**9+7
ans=3
for i in range(1,n):
  if i==1 or s1[i-1]==s2[i-1]:
    ans*=2
  elif not s1[i-1]==s1[i] and not s1[i]==s2[i]:
    ans*=3
print(ans%mod)