#create date: 2020-06-30 09:34

import sys
stdin = sys.stdin
from collections import Counter

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

def main():
    n = ni()
    prime_count = Counter(prime_decomposition(n))
    ans = 0
    for p in prime_count.values():
        i = 1
        while p - i >= 0:
            p -= i
            ans += 1
            i += 1
    print(ans)


if __name__ == "__main__":
    main()