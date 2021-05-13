def euclid(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# ABC148C

a, b = map(int, input().split())
print(a * b // euclid(a, b))
