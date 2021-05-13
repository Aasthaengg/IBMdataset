import math

n = int(input())
a = []
for i in range(5):
  a.append(int(input()))
  
mi = min(a)
ans = 5

ans += math.ceil((n-mi)/mi)

print(ans)