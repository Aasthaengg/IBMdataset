import math

N = int(input())

f = math.factorial(N)
i = 2
ans = 1
cnt = 0

while f != 1:
    if f % i == 0:
        f //= i
        cnt += 1
    else:
        ans *= (cnt + 1)
        cnt = 0
        i += 1


print(ans * (cnt + 1) % (10 ** 9 + 7))