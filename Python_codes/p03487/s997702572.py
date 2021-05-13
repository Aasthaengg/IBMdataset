from collections import Counter

N=int(input())
a=Counter(map(int,input().split()))
ans=0
for keys,values in a.items():
  if keys>values:
    ans+=values
  elif keys<values:
    ans+=values-keys
print(ans)
