a, b = map(int, input().split())
x = abs(a - b)
if x % 2:
    print('IMPOSSIBLE')
else:
    print(int(abs(a+b)/2))