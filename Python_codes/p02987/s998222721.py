S = input()
if S[0] == S[1] and S[1] == S[2]:
  print("No")
elif S[0] == S[1] and S[2] == S[3]:
  print("Yes")
elif S[0] == S[2] and S[1] == S[3]:
  print("Yes")
elif S[0] == S[3] and S[1] == S[2]:
  print("Yes")
else:
  print("No")
