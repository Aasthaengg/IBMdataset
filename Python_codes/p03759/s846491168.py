a = [int(_) for _ in input().split()]
if all(1 <= i <= 100 for i in a):
    print('YES' if a[1] - a[0] == a[2] - a[1] else 'NO')
else:
    print('hoge!')