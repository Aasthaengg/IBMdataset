N,M,X,Y = map(int,input().split())
x = max(X,max(map(int,input().split())))
y = min(Y,min(map(int,input().split())))
a = "War"

for z in range(-101,101):
  if x<z<=y:
    a = "No War"

print(a)