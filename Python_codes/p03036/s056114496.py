r,D,x2000 = map(int,input().split())
x = [0]*10
for i in range(10):
  if i == 0:
    x[i] = r*x2000-D
    print(x[i])
  else:
    x[i] = r*x[i-1]-D
    print(x[i])