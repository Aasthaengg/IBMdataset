from math import ceil
r,g,b,n = map(int, input().split())

ans = 0
for i in range(ceil(n/r)+1):
  for j in range(ceil(n/g)+1):
    if n - (r*i + g*j) >= 0 and (n - (r*i + g*j)) % b == 0: ans += 1
print(ans)