def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    divisors.reverse()
    return divisors
n, m = map(int, input().split())
l = make_divisors(m)
for i in l:
    if m / n >= i:
        print(i)
        exit()
print(1)