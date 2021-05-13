N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

for i in range(N):
  
  if B[i]>A[i]:
    cnt+=A[i]
    r = B[i]-A[i]
  else:
    cnt+=B[i]
    r = 0
  
  if r>A[i+1]:
    cnt+=A[i+1]
    A[i+1]=0
  else:
    cnt+=r
    A[i+1]-=r

print(cnt)