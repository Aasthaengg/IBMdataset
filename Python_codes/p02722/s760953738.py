import math

def get_divisor(n):
    sn = math.sqrt(n)
    i = 1
    divisor = []
    while i <= sn:
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)
        i += 1
    return divisor

n = int(input())
if n == 2:
    print(1)
    exit()
d1 = get_divisor(n)
d2 = get_divisor(n - 1)
ans = -1
for i in d1:
    tmp = int(n)
    if i == 1:
        continue
    while tmp % i == 0:
        tmp //= i
    if tmp % i == 1:
        ans += 1
ans += len(d2)
print(ans)