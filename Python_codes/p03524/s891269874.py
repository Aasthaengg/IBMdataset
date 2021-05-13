S=input()
k=S.count('a')
l=S.count('b')
m=S.count('c')

if abs(k-l)<=1 and abs(l-m)<=1 and abs(m-k)<=1:
    print('YES')
else:
    print('NO')