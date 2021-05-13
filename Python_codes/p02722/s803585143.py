def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

N = int(input())
ans = 0
divs = make_divisors(N)
divs = [x for x in divs if x > 1]
for k in divs:
    x = N
    while x % k == 0:
        x //= k
    if x % k == 1:
        ans += 1

divs = make_divisors(N - 1)
divs = [x for x in divs if x > 1]
ans += len(divs)
print(ans)
