n = int(input())
t = n // 10
n -= t*10
if t==9:
    print('Yes')
elif n == 9:
    print('Yes')
else:
    print('No')
