s=input()
flag_c=False
flag_f=False
for i in range(len(s)):
  if s[i]=="C":
    flag_c=True
  if s[i]=="F" and flag_c:
    print("Yes")
    flag_f=True
    break
if not flag_f:
  print("No")