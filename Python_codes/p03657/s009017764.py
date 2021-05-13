a = input().split()
if int(a[0]) % 3 == 0 or int(a[1]) % 3 == 0 or (int(a[0]) + int(a[1])) % 3 == 0:
    print('Possible')
else:
    print('Impossible')