def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    # divisors.sort()
    return divisors
n = int(input())
res = 0
for x in make_divisors(n):
    x = x-1
    if x == 0:
        continue
    if n % x == n // x:
        res += x
print(res)