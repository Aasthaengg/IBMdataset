s = input()
l = ""
for i in range(3):
  if s[i] == "1":
    l += "9"
  else:
    l += "1"
    
print(int(l))