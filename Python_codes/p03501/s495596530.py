n, a, b = map(int, input().split())
if 1 <= n <= 20 and 1 <= a <= 100 and 1 <= b <= 2000:
    print(min(a * n, b))
else:
    print('hoge!')