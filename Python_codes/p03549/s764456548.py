n, m = map(int, input().split())
n_e = int(1/((1/2)**m))
print((n-m) * 100 * n_e + 1900*n_e*m)
