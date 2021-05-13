N = int(input())
ans = []

for A in range(1,1+int(N/2)):
  tmp = 0
  B = N - A
  A = str(A)
  B = str(B)
  for i in range(0,len(A)):
    tmp += int(A[i])
  for i in range(0,len(B)):
    tmp += int(B[i])
  ans.append(tmp)

print(min(ans))