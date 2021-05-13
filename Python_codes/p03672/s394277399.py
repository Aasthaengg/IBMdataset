s=input()

if len(s)%2:
  s=s[:-1]
else:
  s=s[:-2]

while len(s)!=2:
  if s[:len(s)//2]==s[len(s)//2:]:
    break
  s=s[:-2]
print(len(s))