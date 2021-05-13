t = input()
lst = []
for i in range(len(t)):
  if t[i] == "P":
    lst.append("P")
  else:
    lst.append("D")
    
print(''.join(lst))