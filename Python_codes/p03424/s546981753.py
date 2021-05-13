N = int(input())
arare = input().split()
y = 0
for i in range(len(arare)):
  if arare[i] == "Y":
    y += 1
    break
if y == 1:
  print("Four")
else:
  print("Three")
