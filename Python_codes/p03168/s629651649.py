n = int(input())
p = list(map(float,input().split()))
x = [0]*(n+1)
x[0] = 1
for i in range(n):
  y = [0]*(n+1)
  for j in range(i+1):
    y[j] += x[j]*(1-p[i])
    y[j+1] += x[j]*p[i]
  x = y
print(sum(x[n//2+1:]))