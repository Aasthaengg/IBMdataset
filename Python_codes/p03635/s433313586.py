n = [int(_) for _ in input().split()]
if len(n) == 2 and all(2 <= item <= 100 for item in n):
    print((n[0] - 1) * (n[1] - 1))
else:
    print('hoge!')