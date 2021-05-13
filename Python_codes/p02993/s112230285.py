x=input()
b=x[0]
for i in x[1:]:
  if b==i:
    print("Bad")
    break
  b=i
else:
  print("Good")