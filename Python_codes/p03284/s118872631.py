n, k = map(int, input().split())
if 1 <= n <= 100 and 1<= k <= 100:
    if 0 == n % k:
        print(0)
    else:
        print(1)
else:
    print('hoge!')