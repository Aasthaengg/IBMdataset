#!/usr/bin/env python3
import sys
input = sys.stdin.readline

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n, k = map(int, input().split())
a = [int(item) for item in input().split()]
total = sum(a)

div = divisors(total)
ans = 1
for d in div:
    modd = []
    for item in a:
        modd.append(item % d)
    modd.sort(reverse=True)
    plus = sum(modd)
    opr = 0
    for i, item in enumerate(modd):
        if plus == 0:
            opr += sum(modd[i:])
            break
        plus -= d
        opr += d - item 

    if opr <= k * 2:
        ans = max(ans, d)
print(ans)