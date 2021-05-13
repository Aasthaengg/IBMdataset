a = input()
x = ['2','4','5','7','9']
y = ['0','1','6','8']
z = ['3']
if len(a) == 1:
    if a in x:
        print('hon')
        exit()
    elif a in y:
        print('pon')
        exit()
    elif a in z:
        print('bon')
        exit()

a = a[::-1]
if a[0] in x:
        print('hon')
elif a[0] in y:
        print('pon')
elif a[0] in z:
        print('bon')