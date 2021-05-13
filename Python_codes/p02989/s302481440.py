n=int(input())
l=list(map(int,input().split()))
l.sort()
a=int(n/2)
s=l[a-1]
t=l[a]
if s==t:
  print("0")
else:
  ans=t-s
  print(ans)