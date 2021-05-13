S=input()
T=list(S)
U=list(set(T))
b=[0]*2
if len(U)==2:
  for x in range(4):
    if U[0]==S[x]:
      b[0]+=1
    elif U[1]==S[x]:
      b[1]+=1
  if b[0]==2 and b[1]==2:
    print("Yes")
  else:
    print("No")
else:
  print("No")