# coding: utf-8
# Your code here!
n=int(input())
s=list(map(int,input().split()))
s.sort()
ans=0
for i in range(n):
  for j in range(n):
    if s[i]<s[j]:
      for k in range(n):
        if s[j]<s[k] and s[i]+s[j]>s[k]:
          ans+=1
print(ans)

