s = input()
i = 0
for i in range(len(s)):
  if s[i] == "C":
    if "F" in s[i:]:
      print("Yes")
      exit()
print("No")
