# coding: utf-8
# Your code here!

n = int(input())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

D1 = 0
D2 = 0
D3 = 0
max = 0
for i in range(n):
   diff = abs(X[i] - Y[i])
   D1 += diff
   D2 += diff**2
   D3 += diff**3
   if diff > max:
      max = diff

print('{:.6f}'.format(D1))
print(D2**(1 / 2))
print(D3**(1.0 / 3.0))
print('{:.6f}'.format(max))
