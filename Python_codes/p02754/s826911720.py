n, a, b = list(map(int, input().split()))
pair = n // (a + b)
frac = n % (a + b)
frac_red = a if frac >= a else frac
print(pair * a + frac_red)