k = int(input())
a, b = map(int, input().split())

ans = False
tmp = k

while tmp <= b:
    if (tmp >= a) and (tmp <= b):
        ans = True
        break
    else:
        tmp += k

if ans:
    print('OK')
else:
    print('NG')
