a = list(input())
b = list(input())

a = [int(a[i]) for i in range(len(a))]
b = [int(b[i]) for i in range(len(b))]

flag = True
if len(a) > len(b):
    print('GREATER')
    flag = False
elif len(b) > len(a):
    print('LESS')
    flag = False
else:
    for i in range(len(a)):
        if a[i] > b[i]:
            print('GREATER')
            flag = False
            break
        elif b[i] > a[i]:
            print('LESS')
            flag = False
            break
if flag:
    print('EQUAL')
