a = list(map(int, input().split(' ')))
b = a[0] * a[1]
r = 'Even' if (b % 2 == 0) else 'Odd'
print(r)
