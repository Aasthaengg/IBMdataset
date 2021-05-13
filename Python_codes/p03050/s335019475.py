N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


divs = make_divisors(N)

s = set()
for div in divs:
    if div == 1:
        continue
    a, b = divmod(N, div - 1)
    if a == b:
        s.add(div - 1)

print(sum(s))

