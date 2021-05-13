s = input()
x = 0
y = 0
for i in range(len(s)):
  if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
    x = x + 1
  else:
    if y < x:
      y = x
    x = 0
if y < x:
  y = x
print(y)