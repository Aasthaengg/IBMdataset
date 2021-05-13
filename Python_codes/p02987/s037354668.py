a = input()
b = True
for i in set(a):
  if a.count(i) == 2:
    b = "Yes"
  else:
    b = "No"
print(b)

    
