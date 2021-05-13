s = input()
c = 0
for i in range(3):
  if s[i] == "R":
    c += 1
if c == 2:
  if s[1] == "S":
    print(1)
  else:
    print(2)
else:
  print(c)