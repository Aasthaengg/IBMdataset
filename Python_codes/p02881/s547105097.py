def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

N = int(input())
div = make_divisors(N)
ans = 10 ** 13
for d in div:
    ans = min(ans, d + N // d - 2)
print(ans)
