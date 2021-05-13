A,B,C,K = map(int,input().split())
ans = 0

if K<A:
  ans+=K
  print(ans)
  exit()
else:
  ans+=A
  K-=A
  
if K<B:
  print(ans)
  exit()
else:
  K-=B
  
if K<C:
  ans+=K*(-1)
  print(ans)
else:
  ans+=C*(-1)
  print(ans)