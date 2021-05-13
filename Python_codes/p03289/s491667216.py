s = input()

if s[0] != "A":
  print("WA")
  exit()
if s[2:-1].count("C") != 1:
  print("WA")
  exit()
t = s.index("C")
if s[1:t].islower() == False or s[t+1:].islower() == False:
  print("WA")
  exit()
print("AC")