N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = B[A[0]-1]

for n in range(1,N):
  if A[n]!=1+A[n-1]:
    ans+=B[A[n]-1]
  else:
    ans+=B[A[n]-1]+C[A[n]-2]

print(ans)