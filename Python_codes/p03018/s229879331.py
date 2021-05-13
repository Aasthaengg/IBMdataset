s = input()
s = s.replace("BC", "D")
gomi = 0
c = 0
for i in s:
  if i == "A":
      c += 1
  elif i == "D":
      gomi += c
  else:
      c = 0
print(gomi)