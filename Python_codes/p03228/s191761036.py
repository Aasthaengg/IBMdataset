a, b, k = map(int, input().split(' '))
for i in range(0, k):
    if i % 2 == 0:
        if a % 2 != 0:
            a -= 1
        b += a // 2
        a -= a//2
    else:
        if b % 2 != 0:
            b -= 1
        a += b // 2
        b -= b//2
print(f'{max(0,a)} {max(0,b)}')
