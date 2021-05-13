k,a,b=map(int,input().split())

num=b-a
ans=0

if num <= 2:
  print(1+k)
else:
  ans=(a-1)
  k-=(a-1)
  s=k//2
  l=k%2
  ans=s*num+l+a
  print(ans) 
 