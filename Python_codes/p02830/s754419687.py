N = int(input())
A,B = input().split()
ANS = ''
for i in range(N):
  ANS += A[i]+B[i]
print(ANS)