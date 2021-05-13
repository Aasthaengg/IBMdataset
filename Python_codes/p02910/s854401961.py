S = input()

for s in S[0::2]:
  if s not in "RUD":
    print("No")
    exit()

for t in S[1::2]:
  if t not in "LUD":
    print("No")
    exit()
    
print("Yes")