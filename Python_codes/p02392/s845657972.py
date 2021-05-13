a = input().split()

if int(a[0]) < int(a[1]):
    if int(a[1]) < int(a[2]):
        print('Yes')
    else:
        print('No')
else:
    print('No')
