s = input()

sa = s[::2]
sb = s[1::2]

for i in sa:
  if i == "L":
    print("No")
    exit()

for j in sb:
  if j == "R":
    print("No")
    exit()
print("Yes")