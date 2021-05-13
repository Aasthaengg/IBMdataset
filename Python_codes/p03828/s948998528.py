import math
n = int(input())
mod = 10**9 +7
ans = 1
k = 1
i = 2
N = math.factorial(n)

while N != 1:
    if N%i == 0:
        N = N//i
        k += 1
    else:
        ans *= k
        k = 1
        i += 1
ans *= k
print(ans%mod)
