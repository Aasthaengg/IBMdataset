N=int(input())
S=input()
if len(S)%2==1:
  print("No")
else:
  t=len(S)//2
  if S[0:t]==S[t:len(S)]:
    print("Yes")
  else:
    print("No")