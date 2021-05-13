N=int(input())
A=list(map(int, input().split()))
if N==1:
  print(A[0])
  exit()
tmp=0
for i in range(N):
  tmp+=1/A[i]
print(1/tmp)