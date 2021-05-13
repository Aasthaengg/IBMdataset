s = input()

ac = s.count('a')
bc = s.count('b')
cc = s.count('c')

if max([ac, bc, cc])-min([ac, bc, cc])<=1:
    print('YES')
else:
    print('NO')