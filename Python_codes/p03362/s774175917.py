import math
def prime_numbers(x):
    if x < 2:
        return []
    prime_numbers = [i for i in range(x)]
    prime_numbers[1] = 0
    for prime_number in prime_numbers:
        if prime_number > math.sqrt(x):
            break
        if prime_number == 0:
            continue
        for composite_number in range(2 * prime_number, x, prime_number):
            prime_numbers[composite_number] = 0
    return [prime_number for prime_number in prime_numbers if prime_number != 0]
n = int(input())
primes = prime_numbers(55555)
ans = []
cnt = 0
for i in primes:
    if i % 5 == 1:
        ans.append(i)
        cnt += 1
    if cnt == n:
        exit(print(*ans))