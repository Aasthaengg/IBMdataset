import collections 
a=[]
n=int(input())
for i in range(n):
  S=input()
  s=list(S)
  s.sort()
  b="".join(s)
  a.append(b)
c=collections.Counter(a)
ans=0
for i in c:
  ans+=c[i]*(c[i]-1)//2
print(ans)