S = input()

check = True
for i in range(3):
  if S[i] == S[i+1]:
    check = False
    
if check:
  print("Good")
else:
  print("Bad")