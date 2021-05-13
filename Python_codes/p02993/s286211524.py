inp = list(input())
hard = 0
for number in range(0, 3) :
  if inp[number] == inp[number + 1] :
    hard = 1
    
if hard == 0 :
  print("Good")
else :
  print("Bad")