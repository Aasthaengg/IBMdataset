from collections import Counter
mod=pow(10,9)+7
n=int(input())
s=input()
cs=Counter(s)
ans=1
for a in cs.values():
  ans*=a+1
  ans%=mod
print(ans-1)