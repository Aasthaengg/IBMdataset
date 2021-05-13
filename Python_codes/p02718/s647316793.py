N,M = map(int,input().split())
A = list(map(int,input().split()))
sumA = sum(A)
count = 0
judge = sumA / (4*M)
for i in range(len(A)):
  if A[i] >= judge:
    count += 1
if count < M:
  ans = "No"
else:
  ans = "Yes"
print(ans)