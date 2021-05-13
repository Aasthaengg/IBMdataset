a = [int(_) for _ in input().split()]
if len(a) == 2 and -1000 <= a[0] <= 1000 and -1000 <= a[1] <= 1000:
    print(max(a[0] + a[1], a[0] - a[1], a[0] * a[1]))
else:
    print('hoge!')