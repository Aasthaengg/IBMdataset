A,B,C=map(str,input().split())
#print(sorted(B)[0])
if A[::-1][0]==B[0] and B[::-1][0]==C[0]:
    print('YES')
else:
    print('NO')
