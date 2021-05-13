import math

n = int(input())
x = [float(num) for num in input().split()  ]
y = [float(num) for num in input().split()  ]

delta = []
for i in range(n):
  dif = abs(x[i]-y[i])
  delta.append(dif)

dp1 = sum(delta)
print(dp1)

dp2 = 0.0
for i in range(n):
  dp2 += delta[i]**2
dp2 = math.sqrt(dp2)
print(dp2)

dp3 = 0.0
for i in range(n):
  dp3 += delta[i]**3
dp3 = math.pow(dp3,1/3)
print(dp3)

dpe = 0.0
for i in range(n):
  dpe = max(dpe,delta[i])
print(dpe)

