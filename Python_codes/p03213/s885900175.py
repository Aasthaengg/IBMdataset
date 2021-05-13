from collections import defaultdict
from collections import Counter


def prime_factorization(divs, n):
    while n % 2 == 0:
        divs[2] += 1
        n //= 2

    i = 3
    while i <= int(n ** .5) + 1:
        while n % i == 0:
            divs[i] += 1
            n //= i
        i += 2
    if n != 1:
        divs[n] += 1

    return divs


def num(m):
    return sum([value if key >= m else 0 for key, value in cnt_divs.items()])


N = int(input())
divs = defaultdict(int)
for n in range(2, N + 1):
    divs = prime_factorization(divs, n)

cnt_divs = Counter(divs.values())

print(num(74) + \
      num(24) * (num(2) - 1) + \
      num(14) * (num(4) - 1) + \
      num(4) * (num(4) - 1) * (num(2) - 2) // 2)
