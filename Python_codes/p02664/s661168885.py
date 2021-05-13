s = input()
j = ""
for i in range(len(s)):
  if s[i] == "?":
    j = j + "D"
  else:
    j = j + s[i]
print(j)