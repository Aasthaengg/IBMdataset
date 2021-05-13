N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = sum(A)
SB = sum(B)

cnt_a, cnt_b = 0, 0
for i in range(N):
  if A[i] <= B[i]:
    cnt_a += (B[i] - A[i] + 1)//2
  else:
    cnt_b += A[i] - B[i]

if SB - SA >= max(cnt_a, cnt_b):
  print("Yes")
else:
  print("No")