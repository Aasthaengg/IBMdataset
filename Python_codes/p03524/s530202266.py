s=input()

a=s.count('a')
b=s.count('b')
c=s.count('c')

if max([a,b,c])-min([a,b,c])>=2:
    print('NO')
else:
    print('YES')