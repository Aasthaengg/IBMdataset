s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')

L = [a,b,c]
print('YES' if max(L)-min(L) < 2 else 'NO')
