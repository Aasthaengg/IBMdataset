a = input()
b = input()
a = a + a[:-1]
if b in a:
    print('Yes')
else:
    print('No')

