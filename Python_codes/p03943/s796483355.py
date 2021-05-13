packs = input()
new_packs = packs.split(" ")
a = int(new_packs[0])
b = int(new_packs[1])
c = int(new_packs[2])
if a + b == c or b + c == a or a + c == b:
  print("Yes")
else:
  print("No")