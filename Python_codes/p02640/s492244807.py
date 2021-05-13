X, Y = map(int, input().split())

turu = 4*X-Y
kame = Y-2*X

if turu % 2 == 0 and turu >= 0 and kame % 2 == 0 and kame >= 0:
    print('Yes')
else:
    print('No')