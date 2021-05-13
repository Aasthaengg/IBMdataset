from decimal import Decimal
n,m = map(int,input().split())
A = list(map(int,input().split()))
border = float(sum(A)/(4*m))
border2 = str(border)
border3 = Decimal(border2)
ans = 0
judge = 0
for i in range(n):
  if A[i] >= border3:
    ans+=1
if ans >= m:
  print("Yes")
else:
  print("No")
