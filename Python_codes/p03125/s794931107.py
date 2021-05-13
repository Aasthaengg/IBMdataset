a, b = map(int, input().split())
if a <= a <= b <= 20:
    if 0 == b % a:
        print(a + b)
    else:
        print(b - a)
else:
    print('hoge')