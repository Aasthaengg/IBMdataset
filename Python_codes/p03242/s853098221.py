s = input()

t = ""

for i in range(3):
  if s[i] == "1":
    t += "9"
  else:
    t += "1"
    
print(t)