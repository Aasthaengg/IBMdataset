a = [int(_) for _ in input().split()]
if all(1 <= item <= 100 for item in a):
    print('Possible' if 0 == a[0] % 3 or 0 == a[1] % 3 or 0 == (a[0]+a[1]) % 3 else 'Impossible')
else:
    print('hoge!')