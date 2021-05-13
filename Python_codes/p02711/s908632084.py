n = input()
for i in range(3):
  if n[i] == "7":
    print("Yes")
    break
  elif i==2 and n[i]!="7":
    print("No")