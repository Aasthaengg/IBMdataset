A=input()
if A[0] != "A":
  print("WA")
  quit()
if A[2:-1].count("C") != 1:
  print("WA")
  quit()
for i in range(1,len(A)):
  if A[i] !="C" and not A[i].islower():
    print("WA")
    break
else:
  print("AC")