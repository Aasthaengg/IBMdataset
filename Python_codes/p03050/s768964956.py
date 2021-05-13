def solve(n):
    res = 0
    p = 1
    while p**2 <= n:
        if n % p == 0:
            m = n // p - 1
            if m > p:
                res += m
        p += 1
    return res

n = int(input())
print(solve(n))