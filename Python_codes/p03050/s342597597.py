import math
n = int(input())
ans = 0
for i in range(1,math.ceil(math.sqrt(n))):
    if n % i == 0:
        div = (n - i) // i
        if div > i:
            ans += div
print(ans)
