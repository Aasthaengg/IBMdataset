a, b = map(int, input().split())
if 1 <= a <= 9 and 1 <= b <= 9:
    print(a + b if a + b < 10 else 'error')
else:
    print('hoge!')