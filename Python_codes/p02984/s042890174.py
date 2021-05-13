n = int(input())
D = list(map(int,input().split()))
Y = [0]*n

for i in range(n):
  if i%2==0:
    Y[0] += D[i]
  else:
    Y[0] -= D[i]

for i in range(1,n):
  Y[i] = 2*D[i-1] - Y[i-1]

print(*Y)