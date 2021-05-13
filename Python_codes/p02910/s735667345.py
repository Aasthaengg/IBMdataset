s = input()
n = len(s)
for i in range(0,n,2):
  if s[i] == "L":
    print("No")
    break
else:
  for j in range(1,n,2):
    if s[j] == "R":
      print("No")
      break
  else:
    print("Yes")