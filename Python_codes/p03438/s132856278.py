N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

countA,countB = 0,0

for i in range(N):
  if A[i] <= B[i]:
    countA += (B[i]-A[i])//2
  else:
    countB += A[i]-B[i]
if countA >= countB:
  ans = "Yes"
else:
  ans = "No"

print(ans)