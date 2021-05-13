a = input()
b = input()
a = a.zfill(101)
b = b.zfill(101)
if a<b:
    print('LESS')
elif a>b:
    print('GREATER')
else:
    print('EQUAL')