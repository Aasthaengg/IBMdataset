x, y = map(int, input().split())

flg = -1

for i in range(x + 1):
    if y == -2*i + 4*x:
        flg = 1

if flg == 1:
    print('Yes')
else:
    print('No')