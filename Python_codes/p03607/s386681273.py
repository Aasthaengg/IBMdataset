import collections
n=int(input())
lst=[int(input()) for i in range(n)]
xs=list(set(lst))
ans=0
lst=collections.Counter(lst)
for i in xs:
  if lst[i]%2==1:
    ans+=1

print(ans)
