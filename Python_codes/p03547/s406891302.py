X, Y = input().split()
o = '0123456789ABCDEF'
if o.index(X) < o.index(Y):
    print('<')
elif o.index(X) > o.index(Y):
    print('>')
else:
    print('=')