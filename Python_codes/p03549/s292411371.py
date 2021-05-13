n, m = map(int, input().split())

t = 1900 * m + 100 * (n-m)
r = (1/2) ** m

print(int(t/r))
