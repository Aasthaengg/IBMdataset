N = int(input())
S = input()
s = list(S)
 
cou = s.count("R")
if cou > N / 2:
  print("Yes")
else:
  print("No")