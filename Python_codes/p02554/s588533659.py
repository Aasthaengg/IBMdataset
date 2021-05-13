n = int(input())
p = 10**9+7
print((pow(10, n, p) - 2*pow(9, n, p) + pow(8, n, p)) % p)