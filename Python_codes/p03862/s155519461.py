N,x = map(int,input().split())
A = list(map(int,input().split()))
pre = 0
ans = 0

for a in A:
  eat = max(0,pre+a-x)
  pre = a - eat
  ans+= eat

print(ans)