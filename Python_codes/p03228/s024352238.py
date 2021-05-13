a, b, k = map(int, input().split())

flag = True
for i in range(k):
    if flag:
        if a % 2 == 1:
            a -= 1
        b += a // 2
        a = a // 2
        flag = False
    else:
        if b % 2 == 1:
            b -= 1
        a += b // 2
        b = b // 2
        flag = True
print(a, b)