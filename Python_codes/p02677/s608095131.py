import math

A, B, H, M = map(int, input().split())
Mth = 6*M
Hth = 30*H + M/2
th = math.pi*abs(Mth-Hth)/180

x = A**2+B**2-2*A*B*math.cos(th)
result = math.sqrt(x)
print(result)