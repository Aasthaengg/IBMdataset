n = int(input())
flg = False

if n % 7 == 0:
    flg = True
else:
    for i in range(int(n/7) + 1):
        m = n - i * 7
        if m % 4 == 0:
            flg = True
            break

if flg:
    print('Yes')
else:
    print('No')