import math


def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def enum_div(n):
    ldv, udv = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ldv.append(i)
            if i != n // i:
                udv.append(n // i)
        i += 1
    return ldv + udv[::-1]


n = int(input())
cnt = math.inf

if isPrime(n):
    cnt = n - 1
else:
    arr = enum_div(n)
    for i, v in enumerate(range(len(arr) - 1, -1, -1)):
        cnt = min(cnt, arr[i] + arr[v] - 2)

print(cnt)
