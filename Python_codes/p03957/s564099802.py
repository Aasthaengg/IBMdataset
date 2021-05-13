s = input()
is_C = False
for i in range(len(s)):
  if s[i] == "C":
    is_C = True
  if is_C and s[i] == "F":
    print("Yes")
    exit()
  if i == len(s)-1:
    print("No")