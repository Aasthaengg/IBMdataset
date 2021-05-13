def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    return table
A, B, K = map(int, input().split())
res = divisors(A) & divisors(B)
res = list(res)
res.sort()
print(res[-K])