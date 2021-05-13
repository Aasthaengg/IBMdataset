A,B,C = [int(i) for i in input().split()]
Flag = False

for i in range(1,B+1):
    D = i*A % B
    if D == C:
        Flag = True
        break

if Flag == True:
    print('YES')
else:
    print('NO')