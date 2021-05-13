b = list(input())

for i in range(len(b)):
  if b[i] == "A":
    b[i] = "T"
  elif b[i] == "T":
    b[i] = "A"
  elif b[i] == "C":
    b[i] = "G"
  else:
    b[i] = "C"
    
print("".join(b))
