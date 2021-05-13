S = input()
A = S.count('o') 
B = 15 - len(S)
if A+B >= 8:
    print('YES')
else:
    print('NO')