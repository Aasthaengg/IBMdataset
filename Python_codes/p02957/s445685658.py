a, b = map(int,input().split())

k = a + b

if k % 2 == 0:
    print(int(k / 2))

else:
    print('IMPOSSIBLE')