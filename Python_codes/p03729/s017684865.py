A,B,C=map(str,input().split())
ans="NO"
if A[len(A)-1]==B[0] and B[len(B)-1]==C[0]:
    ans="YES"
print(ans)