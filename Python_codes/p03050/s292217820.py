n = int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    #divisors.sort(reverse=True)
    return divisors

D = make_divisors(n)
ans = 0
for d in D:
    m = d-1
    q = n//d
    if m > 0 and 0 <= q < m:
        ans += m
print(ans)
