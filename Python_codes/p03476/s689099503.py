from itertools import accumulate
import sys
input = sys.stdin.buffer.readline


def sieve(n):
    f = []
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    for i in range(n+1):
        if is_prime[i]:
            f.append(i)
    return f


s = sieve(10**5)
s = set(s)
number_2017 = [0]*(10**5+1)

for i in range(1, 10**5+1):
    if i % 2 == 0:
        continue
    if i in s and (i+1)//2 in s:
        number_2017[i] = 1


acc = list(accumulate(number_2017))

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r]-acc[l-1])
