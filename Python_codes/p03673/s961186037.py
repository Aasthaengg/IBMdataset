N=int(input())
A=list(input().split())
if N%2==0:
  B=A[::-1]
  print(' '.join(B[::2])+' ' + ' '.join(A[::2]))
else:
  B=A[::-1]
  A=A[1::2]
  print(' '.join(B[::2])+' ' + ' '.join(A[:]))