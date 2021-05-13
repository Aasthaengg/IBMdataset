from math import factorial
n, m = [int(x) for x in input().split()]
temp = abs(n - m)
if temp > 1:
    print(0)
    exit()
mod = 10 ** 9 + 7
f_n = factorial(n) % mod
f_m = factorial(m) % mod
ans = f_n * f_m % mod
if temp == 0:
    ans = ans * 2 % mod
print(ans)