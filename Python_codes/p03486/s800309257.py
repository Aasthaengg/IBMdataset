S=sorted(input())
T=sorted(input())
for i in range(min(len(S),len(T))):
  if S[i] < T[-1*(i+1)]:
    print("Yes")
    break
  elif S[i] == T[-1*(i+1)]:
    if i+1 == min(len(S),len(T)) and len(S) < len(T):
      print("Yes")
      break
    
  else:
    print("No")
    break
else:
  print("No")