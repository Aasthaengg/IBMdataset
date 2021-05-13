
[X,Y] = list(input().split())

dam = sorted([X,Y])

if X==Y:
    print('=')

elif [X,Y] ==dam:
    print('<')
else:
    print('>')
