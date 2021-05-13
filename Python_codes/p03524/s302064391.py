s = input()
na = s.count('a')
nb = s.count('b')
nc = len(s) - na - nb
if max(na,nb,nc)-min(na,nb,nc)<=1:
    print('YES')
else:
    print('NO')