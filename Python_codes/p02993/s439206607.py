S = list(input())
A = 0
for i in range(0, 3) :
  if S[i] == S[i + 1] :
    A = 1
  
if A == 0 :
  print("Good")
else :
  print("Bad")