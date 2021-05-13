n, m = [int(w) for w in input().split()]

t = 1900 * m + 100 * (n - m)
p = 2 ** m

print(t*p)
