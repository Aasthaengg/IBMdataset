S=input()
b=0
for x in range(3):
  if S[x]==S[x+1]:
    b=1
if b==1:
  print("Bad")
else:
  print("Good")