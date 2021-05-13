N, A, B = map(int,input().split())
if ((A-B)%2==0):
  ans = abs(A-B)//2
elif (N-B <= A-1):
  ans = (2*N -A-B+1)//2
elif (N-B > A-1):
  ans = (B+A-1)//2
print(ans)