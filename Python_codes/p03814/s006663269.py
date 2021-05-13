s=input()
a_min=0
z_max=0
for i in range(len(s)):
  if s[i]=="A":
    a_min=i
    break
for i in range(len(s)):
  if s[i]=="Z":
    z_max=i
print(z_max-a_min+1)