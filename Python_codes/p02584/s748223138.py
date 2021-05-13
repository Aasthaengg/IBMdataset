X,K,D=map(int,input().split())
X=abs(X)
if X/D >= K:
  print(X-D*K)
  exit()
s = X//D
X -= s*D
K -= s
if K%2 == 0:
  print(X)
else:
  print(abs(X-D))