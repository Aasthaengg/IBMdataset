#!/usr/bin/env python3
a, b, k = map(int, open(0).read().split())


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = set(table)
    return table


x = divisor(a)
y = divisor(b)
print(sorted(list(x & y), reverse=True)[k-1])
