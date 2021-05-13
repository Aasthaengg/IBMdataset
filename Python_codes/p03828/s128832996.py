from math import factorial

N = int(input())
N = factorial(N)

i = 2
num = 1
ans = 1

while N != 1:
    if N % i == 0:
        N //= i
        num += 1
    else:
        ans *= num
        num = 1
        i += 1
ans *= num
ans %= (10**9) + 7

print(ans)