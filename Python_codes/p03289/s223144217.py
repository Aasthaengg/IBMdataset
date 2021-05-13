s = input()
ac = True
c = True
if s[0] != "A":
  ac = False
if not ord("a") <= ord(s[1]) <= ord("z"):
  ac = False
if not ord("a") <= ord(s[-1]) <= ord("z"):
  ac = False
for i in range(2, len(s)-1):
  if s[i] == "C":
    if c:
      c = False
    else:
      ac = False
  else:
    if not ord("a") <= ord(s[i]) <= ord("z"):
      ac = False
if c:
  ac = False
if ac:
  print("AC")
else:
  print("WA")
