N = input()
couta = N.count('a')           
coutb = N.count('b')
coutc = N.count('c')
x = abs(couta - coutb)
y = abs(coutb - coutc)
z = abs(couta - coutc)
if max(x,y,z) <= 1:
    print('YES')
else:
    print('NO')