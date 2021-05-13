a, b = input().split()
a = int(a)
q, r = map(int, b.split('.'))
a *= q * 100 + r
a = a // 100
print(a)