n=int(input())
a=list(map(int,input().split()))
maxa=max(a)
mina=min(a)
if abs(mina)<=abs(maxa):
  idx=a.index(maxa)
  print(2*(n-1))
  pre=idx+1
  for i in range(1,n):
    print(pre,i+1)
    print(pre,i+1)
    pre=i+1
elif abs(mina)>abs(maxa):
  idx=a.index(mina)
  print(2*(n-1))
  pre=idx+1
  for i in range(n-1,0,-1):
    print(pre,i)
    print(pre,i)
    pre=i
    
