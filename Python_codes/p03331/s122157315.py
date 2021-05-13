N = int(input())

A = str(N//2)
B = str(N-int(A))

ans1,ans2 = 0,1
for i in range(len(A)):
  ans1 += int(A[i])
for i in range(len(B)):
  ans1 += int(B[i])

B = str(N-1)

for i in range(len(B)):
  ans2 += int(B[i])

ans = min(ans1,ans2)

print(ans)