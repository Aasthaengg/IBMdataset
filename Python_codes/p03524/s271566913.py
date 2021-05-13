S=input()
A=S.count('a')
B=S.count('b')
C=S.count('c')
if A==B and B==C:
    print('YES')
elif A==B:
    if C==A-1 or C==A+1:
        print ('YES')
    else:
        print('NO')
elif B==C:
    if A==B-1 or A==B+1:
        print('YES')
    else:
        print('NO')
elif C==A:
    if B==A-1 or B==A+1:
        print('YES')
    else:
        print('NO')
else:
     print('NO')