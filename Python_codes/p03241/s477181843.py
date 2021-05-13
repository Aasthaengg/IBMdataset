n, m = map(int, input().split())
factors = [1, m]
sqrt = round(m ** 0.5 + 0.5)
for i in range(2, sqrt + 1):
    if not m % i:
        factors.append(i)
        factors.append(m // i)
factors = sorted(factors)
def search(l):
    for i in l:
        if i >= n:
            return m // i
print(search(factors))