A=input()
B=input()
count=0
if A[0]==B[2]:
    if A[1]==B[1]:
        if A[2]==B[0]:
            count+=1
if count>0:
    print('YES')
else:
    print('NO')
