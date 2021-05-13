"""ワット数に気を付けましょう"""
A,B=map(int,input().split())
ans=0
now=1
while now<B:
  ans+=1
  now+=A-1
print(ans)