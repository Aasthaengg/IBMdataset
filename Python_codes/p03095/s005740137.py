import collections
n=int(input())
s=list(input())
s=collections.Counter(s)
ans=1
for i in s:
  ans*=s[i]+1
  ans%=10**9+7
print(ans-1)