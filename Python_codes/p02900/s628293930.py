a, b = map(int,input().split())
#素因数分解
def prime(n):
    i = 2
    table = set()
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.add(i)
        i += 1
    if n > 1:
        table.add(n)
    return table

print(len(prime(a).intersection(prime(b))) + 1)