a, b, c, k = map(int,input().split())

s = abs(a - b)

if len(str(s)) >= 19:
    print('Unfair')
else:
    if k % 2 != 0:
        print(-a + b)
    else:
        print(a - b)