n = list(input())
b = 0
for i in range(3):
  if n[i]=="7":
    print("Yes")
    b += 1
    break
if b==0:
  print("No")