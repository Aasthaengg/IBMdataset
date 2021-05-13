S = input()
T = input()
s = len(S)
t = len(T)
A = []

for i in range(s-t+1):
  if all(S[i+j]==T[j] or S[i+j]=="?" for j in range(t)):
    A.append(S[:i]+T+S[i+t:])

A = [a.replace("?","a") for a in A]

if len(A)==0:
  print("UNRESTORABLE")
else:
  print(min(A))