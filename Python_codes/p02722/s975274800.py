n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

a = make_divisors(n-1)
b = make_divisors(n)

a.remove(1)
b.remove(1)

count = len(a)

for i in b:
    n_new = n // i
    while n_new % i == 0:
        n_new = n_new // i
    if n_new % i == 1:
        count += 1

print(count)