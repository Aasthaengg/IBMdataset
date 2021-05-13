n = int(input())
if n == 0:
    print(0)
    exit()

ret = ''
while n != 0:
    if n % (-2) == 0:
        ret = '0' + ret
    else:
        ret = '1' + ret
        n -= 1
    n /= -2

print(ret)
