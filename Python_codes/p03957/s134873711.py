s = input()
flag = 0
for i in range(len(s)):
  if not flag and s[i] == "C":
    flag = 1
  if flag and s[i] == "F":
    print("Yes")
    quit()
print("No")