a = input().split()

if 0 > int(a[2]) - int(a[4]):
    print('No')
elif 0 > int(a[3]) - int(a[4]):
    print('No')
elif int(a[0]) < int(a[2]) + int(a[4]):
    print('No')
elif int(a[1]) < int(a[3]) + int(a[4]):
    print('No')
else:
    print('Yes')   
