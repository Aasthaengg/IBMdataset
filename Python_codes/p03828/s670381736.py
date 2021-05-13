import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter


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


n = int(readline())
divisors = [1]
for i in range(1, n):
    divisors += prime_decomposition(i + 1)
counter = list(Counter(divisors).items())
ans = 1
mod = 10 ** 9 + 7
for k, v in counter:
    if k != 1:
        ans = (ans % mod) * ((v + 1) % mod) % mod
print(ans)
