import math
n = int(input())
ans = 0
for i in range(1,math.floor(math.sqrt(n))+1):
    if n % i == 0:
        num = (n//i)-1
        if num > 0:
            if n // num == n % num:
                ans += num
print(ans)