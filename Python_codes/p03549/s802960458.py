n, m = map(int, input().split())
s100 = 100*(n - m) * 2**m
s1900 = m * 1900 * 2**m
print(s100 + s1900)