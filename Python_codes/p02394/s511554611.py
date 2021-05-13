z = input()
a = z.split()
if int(a[2]) >= int(a[4]) and int(a[3]) >= int(a[4]) and \
int(a[0]) >= int(a[2])+int(a[4]) and int(a[1]) >= int(a[3])+int(a[4]):
    print('Yes')
else:
    print('No')