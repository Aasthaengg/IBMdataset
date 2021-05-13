s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')
x = (len(s)-1)//3+1
if a <= x and b <= x and c <= x:
    print('YES')
else:
    print('NO')