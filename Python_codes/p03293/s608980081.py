S = input()
T = input()
flag = 0
for i in range(len(T)):
  if S == T:
    flag = 1
    break
  else:
    S = S[len(S)-1] + S[:-1]
if flag == 0:
  print("No")
else:
  print("Yes")