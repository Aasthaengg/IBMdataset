s = list(input())

for i in range(len(s)):
  if (i+1)%2 == 0:
    if s[i] != "R":
      continue
    else:
      print("No")
      exit()
      
  else:
    if s[i] != "L":
      continue
    else:
      print("No")
      exit()
      
print("Yes")