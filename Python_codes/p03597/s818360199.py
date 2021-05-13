n = int(input())
a = int(input())
if 1 <= n <= 100 and 0 <= a <= n ** 2:
    print(n ** 2 - a)
else:
    print('hoge!')