a = [int(input()) for i in range(2)]
if a[0] > a[1]:
    print('GREATER')
elif a[0] == a[1]:
    print('EQUAL')
else:
    print('LESS')