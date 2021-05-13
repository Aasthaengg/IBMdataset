a, b, c = [int(x) for x in input().split()]
print(0 if (a * b *c) % 2 == 0 else min(a * b, b * c, c * a))