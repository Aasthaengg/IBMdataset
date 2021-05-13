import math
m = [int(input()) for _ in range(5)]
ans = 0
b = 0
for i in m:
  ans+=math.ceil(i/10)*10
  if i%10!=0:
    b = max(b, 10-i%10)
print(ans-b)