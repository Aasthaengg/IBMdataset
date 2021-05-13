N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

divs = make_divisors(N)

ans = 0

for d in divs:
    if d == 1:
        continue
    m = d - 1
    if N // m == N % m:
        ans += m

print(ans)


