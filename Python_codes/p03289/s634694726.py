S=input()
if S[0]!="A":
  print("WA")
  exit()
if "C" not in list(S[2:-1]):
  print("WA")
  exit()
S=list(S)
ans=0
for i in S:
  if i.islower()==True:
    ans+=1
if ans!=(len(S)-2):
  print("WA")
  exit()
print("AC")