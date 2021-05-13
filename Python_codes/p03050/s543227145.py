def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

n = int(input())
count = 0
for i in make_divisors(n):
    if i == 1:
        continue
    quotient, remainder = divmod(n, i-1)
    if quotient == remainder:
        count += i-1

print(count)