X,Y = map(str,input().split())

a = ['A','B','C','D','E','F']
b = [10,11,12,13,14,15]

if a.index(X) > a.index(Y):
    print('>')
elif X == Y:
    print('=')
else:
    print('<')