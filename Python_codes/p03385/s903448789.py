n = input()

lst = []
for i in range(3):
  lst.append(n[i])
  
lst.sort()

if lst == ["a", "b", "c"]:
  print("Yes")
else:
  print("No")