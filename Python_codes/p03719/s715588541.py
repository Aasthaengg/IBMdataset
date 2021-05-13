n = [int(_) for _ in input().split()]
if all(-100 <= i <= 100 for i in n):
    print('Yes' if n[0] <= n[2] <= n[1] else 'No')
else:
    print('hoge!')