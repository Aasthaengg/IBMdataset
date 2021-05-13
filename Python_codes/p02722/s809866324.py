n = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors



ansl = make_divisors(n-1)
ansl.remove(1)
for i in make_divisors(n):
    if i == 1:
        continue
    k = n
    while k:
        if k % i == 0:
            k //= i
        else:
            if k % i == 1:
                ansl.append(i)
            break

print(len(set(ansl)))


