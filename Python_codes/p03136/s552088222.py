N = input()
A = list(map(int, input().split()))

M = max(A)
S = sum(A) - M

if M < S:
  print("Yes")
else:
  print("No")