n = int(input())

ans = ''
while n != 0:
    if abs(n) % 2 == 0:
        ans = '0' + ans
    else:
        ans = '1' + ans
    n = (n-1) // -2

if ans == '':
    print(0)
else:
    print(ans)