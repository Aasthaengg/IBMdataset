N,M,X=map(int,input().split())
A=list(map(int,input().split()))
x = 0
for i in range(X,N+1):
  if i in A:
    x += 1
y = 0
for i in range(X+1):
  if i in A:
    y += 1
print(min(x,y))