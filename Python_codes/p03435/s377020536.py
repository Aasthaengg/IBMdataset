A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
ans='Yes'
if A[0]+C[2]!=A[2]+C[0]:
  ans='No'
elif abs(A[0]-A[1])!=abs(B[0]-B[1]) or abs(B[0]-B[1])!=abs(C[0]-C[1]):
  ans='No'
elif abs(A[1]-A[2])!=abs(B[1]-B[2]) or abs(B[1]-B[2])!=abs(C[1]-C[2]):
  ans='No'
elif abs(A[0]-B[0])!=abs(A[1]-B[1]) or abs(A[1]-B[1])!=abs(A[2]-B[2]):
  ans='No'
elif abs(B[0]-C[0])!=abs(B[1]-C[1]) or abs(B[1]-C[1])!=abs(B[2]-C[2]):
  ans='No'
print(ans)