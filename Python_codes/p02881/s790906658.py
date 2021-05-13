import math

n = int(input())
ans = n-1
x = int(math.ceil(math.sqrt(n)))

for i in range(1, x+1):
    if n%i == 0:
        ans = int(min(ans, i+n/i-2))

print(ans)
