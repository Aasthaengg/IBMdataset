n = int(input())

if n == 0:
    print(0)
else:
    cnt, now = 1, 0
    ans = ''
    for i in range(100):
        if n == now:
            break
        if (n - now) % (2**(i + 1)) != 0:
            ans = ans + '1'
            now += pow(-2, i)
        else:
            ans = ans + '0'
    print(ans[::-1])
