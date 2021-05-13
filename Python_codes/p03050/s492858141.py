#!/usr/bin/env python3
def divisor_dif_2_over(n):
    if n == 1:
        return []
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0 and (n // i) - i >= 2:
            res.append(n // i - 1)
        i += 1
    return res


n = int(input())
# print(divisor_dif_2_over(n))
print(sum(divisor_dif_2_over(n)))
