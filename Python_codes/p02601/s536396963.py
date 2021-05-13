a, b, c = map(int, input().split())
n = int(input())

for i in range(n):

    if a >= b:
        b = b * 2
    elif b >= c:
        c = c * 2
    else:
        print('Yes')
        exit(0)

if a < b < c:
    print('Yes')
else:
    print('No')
