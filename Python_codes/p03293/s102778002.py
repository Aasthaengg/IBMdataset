s = input()
t = input()
if s == t:
  print("Yes")
  exit()
for i in range(1,len(s)):
  if s[len(s)-i:]+s[:len(s)-i] == t:
    print("Yes")
    exit()
print("No")