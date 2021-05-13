s=input()
while s[0]!="A":
  s=s[1:]
while s[-1]!="Z":
  s=s[:-1]
print(len(s))