X,Y = input().split()

S=[X,Y]
S.sort()

if X==Y:
  print("=")
else:
  if S[0]==X:
    print("<")
  elif S[0]==Y:
    print(">")