s = str(input())
L = [s.count('a'), s.count('b'), s.count('c')]
if max(L) - min(L) <= 1:
    print('YES')
else:
    print('NO')
