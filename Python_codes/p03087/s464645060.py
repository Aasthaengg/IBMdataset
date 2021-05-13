import bisect
n,q=map(int,input().split())
s=input()
a=[]
for i in range(n-1):
  if s[i:i+2]=='AC':
    a.append(i)
for _ in range(q):
  l,r=map(int,input().split())
  print(bisect.bisect(a,r-1.5)-bisect.bisect(a,l-1.5))