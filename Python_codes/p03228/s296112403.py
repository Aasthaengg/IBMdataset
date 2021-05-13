a, b, k = map(int, input().split())

flg = 1

for i in range(k):
    if flg == 1:
        if a % 2 == 0:
            b += a // 2
            a /= 2
        else:
            a -= 1
            b += a // 2
            a /= 2
    elif flg == -1:
        if b % 2 == 0:
            a += b // 2
            b /= 2
        else:
            b -= 1
            a += b // 2
            b /= 2
    flg *= -1

print(int(a), int(b))