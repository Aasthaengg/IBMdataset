N=int(input())
SUM=0
for i in range(N):
  x,u=input().split()
  x=float(x)
  if u=='BTC':
    x *= 380000.0
  SUM += x
print(SUM)