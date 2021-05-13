S=input()
T=input()
if len(S)+1 ==len(T):
  if S[0:len(S)]==T[0:len(T)-1]:
    print("Yes")
  else:
    print("No")
else:
  print("No")