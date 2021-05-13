#!/usr/bin/env python3
n = int(input())
# 長さN になるまで、%5 = 1となる整数を列挙する
def sleve_of_Eratosthenes(n):
    # N 以下の素数を全列挙
    res = []
    if n == 1:
        return res
    ok = [False] * (1 + n)
    for i in range(2, n + 1):
        if ok[i]:
            continue
        tmp = 1
        res.append(i)
        while tmp * i <= n:
            ok[tmp * i] = True
            tmp += 1
    return res


prime = sleve_of_Eratosthenes(55555)
len_arr = 0
arr = []
for a in prime:
    if a % 5 == 1:
        arr.append(a)
        len_arr += 1
        if len_arr == n:
            break
print(*arr)
