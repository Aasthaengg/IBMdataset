n = int(input())

if n == 0:
    print(0)
    exit()

ans = ''

flag = True

while n != 0:
    if abs(n % 2) == 1:
        ans += '1'
        if flag:
            n -= 1
        else:
            n += 1
    else:
        ans += '0'

    n = n // 2
    flag = not flag

print(ans[::-1])