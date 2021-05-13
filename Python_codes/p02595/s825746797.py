N, D = map(int,input().split())
X, Y = [],[]
for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
assert len(X) == N

print(len([(x,y) for x,y in zip(X,Y) if x ** 2 + y ** 2 <= D ** 2]))