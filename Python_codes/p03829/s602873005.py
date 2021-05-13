N,A,B = map(int,input().split())
X = list(map(int,input().split()))
ans = 0

for x1,x2 in zip(X[0:],X[1:]):
  ans+=min(A*(x2-x1),B)

print(ans)