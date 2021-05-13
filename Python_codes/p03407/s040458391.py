a, b, c = map(int, input().split())
if 1 <= a <= 500 and 1 <= b <= 500 and 1 <= c <= 1000:
    if a + b >= c:
        print('Yes')
    else:
        print('No')
else:
    print('hoge!')