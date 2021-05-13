S=input()
if len(S)%2!=0:
  print("No")
  exit()
for i in range(int(len(S)/2)):
  if S[i*2]!="h":
    print("No")
    exit()
  if S[i*2+1]!="i":
    print("No")
    exit()
print("Yes")