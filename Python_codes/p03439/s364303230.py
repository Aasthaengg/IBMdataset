def nexts(X,Xs,Y,Ys):
    Z = (X+Y)//2
    print('{}\n'.format(Z))
    Zs = input()
    if Zs == 'Vacant':
        sys.exit()
    if (Xs == Zs and (Z-X)%2 == 1)\
    or (Xs != Zs and (Z-X)%2 == 0):
        Y, Ys = Z, Zs
    else:
        X, Xs = Z, Zs
    return X,Xs,Y,Ys

import sys

N = int(input())
print('0\n')
xs = input()
if xs == 'Vacant':
    sys.exit()
print('{}\n'.format(N-1))
ys = input()
if ys == 'Vacant':
    sys.exit()
x, y = 0, N-1
while True:
    x,xs,y,ys = nexts(x,xs,y,ys)