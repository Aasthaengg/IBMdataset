k = int(input())
a, b = map(int, input().split())
if a == b == k:
    print('OK')
elif a == b and a % k == 0:
    print('OK')
else:
    for i in range(a, (b+1)):
        if i % k == 0:
            print('OK')
            break
    else:
        print('NG')