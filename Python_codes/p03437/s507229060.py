X,Y = map(int,input().split())
X_ = X
while X_ <= 10**9:
  if X == Y:
    print(-1)
    exit()
  X_ += X
  if X%Y != 0:
    print(X)
    exit()

print(-1)