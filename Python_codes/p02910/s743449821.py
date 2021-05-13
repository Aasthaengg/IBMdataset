S = input()

for i in S[::2]:
  if i not in "RUD":
    print("No")
    exit()

for i in S[1::2]:
  if i not in "LUD":
    print("No")
    exit()
    

print("Yes")