N,M=map(int,input().split())
A=list(map(int,input().split()))
sm=0
ans=0
l={0:1}
for i in range(len(A)):
  sm=(sm+A[i])%M
  ans+=l.get(sm,0)
  l[sm]=l.get(sm,0)+1
print(ans)