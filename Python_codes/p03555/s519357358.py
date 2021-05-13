C=[0,0]
A=[0,0]
C[0]=list(input())
C[1]=list(input())
A[1]=[C[0][-1],C[0][-2],C[0][-3]]
A[0]=[C[1][-1],C[1][-2],C[1][-3]]
print('YES' if A==C else 'NO')