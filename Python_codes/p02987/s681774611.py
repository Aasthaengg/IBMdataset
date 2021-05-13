S = sorted(input())

if S[0]==S[1]==S[2]==S[3]:
  print("No")
elif S[0]==S[1] and S[2]==S[3]:
  print("Yes")
else:
  print("No")