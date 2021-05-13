P, Q, R = map(int, input().split())
min = P + Q
if P + R < min:
  min = P + R
if Q + R < min:
  min = Q + R
print(min)