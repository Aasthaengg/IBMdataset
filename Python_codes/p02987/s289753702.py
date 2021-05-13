s = input()
s1 = s[:1]
for i in range(1, 4):
  if(s[i:i+1] != s1):
    s2 = s[i:i+1]
if(s.count(s1) == 2 and s.count(s2) == 2):
  print("Yes")
else:
  print("No")
