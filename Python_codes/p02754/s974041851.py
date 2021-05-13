n, a, b = [int(i) for i in input().split()]
l = min(n % (a+b),a)
s = n // (a+b)
print(s*a+l)