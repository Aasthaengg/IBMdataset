import collections
n=int(input())
s=[]
for i in range(n):
  X=''
  Y=sorted(input())
  for i in range(10):
    X+=Y[i]
  s.append(X)
cnt=collections.Counter(s)
ans=0
for i in cnt.values():
  ans+=i*(i-1)//2
print(ans)