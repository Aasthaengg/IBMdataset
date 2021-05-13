a =input()
s = 0
for i in a:
  if i in "+":
    s +=1
  else:
    s -=1
print(s)
