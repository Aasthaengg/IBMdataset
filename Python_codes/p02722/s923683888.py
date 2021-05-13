n = int(input())

def get_divisors(n):
    result = []
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            result.append(i)
            if n != i ** 2:
                result.append(n // i)
    result.sort()
    return result

c = 0
for number in get_divisors(n)[1:]:
    tmp = n
    while tmp % number == 0:
        tmp //= number
    if tmp % number == 1:
        c += 1

c += len(get_divisors(n-1)) - 1
print(c)
