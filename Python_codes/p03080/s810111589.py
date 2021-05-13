N = int(input())
B = 0
R = 0
S = input()
for i in range(N):
  if S[i] == "R":
    R += 1
  else:
    B += 1
if R>B:
  print("Yes")
else:
  print("No")