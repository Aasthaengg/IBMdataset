a, b, c, k = map(int, input().split())

if k % 2 == 0:
    print(a - b if abs(a - b) < 10 ** 18 else 'Unfair')
else:
    print(b - a if abs(b - a) < 10 ** 18 else 'Unfair')

