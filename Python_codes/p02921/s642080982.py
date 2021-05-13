S = input()
T = input()

if S[0] == T[0] and S[1] == T[1] and S[2] == T[2]:
  print(3)
elif S[0] == T[0] and S[1] == T[1] and S[2] != T[2]: 
  print(2)
elif S[0] != T[0] and S[1] == T[1] and S[2] == T[2]: 
  print(2)
elif S[0] == T[0] and S[1] != T[1] and S[2] == T[2]: 
  print(2)
elif S[0] != T[0] and S[1] != T[1] and S[2] != T[2]: 
  print(0)
else:
  print(1)