A,B,C=map(str,input().split())
print('YES'if A[int(len(A))-1]==B[0] and B[int(len(B))-1]==C[0] else 'NO')