s = input()
n = len(s)
if s[0] == "A" and s[2:n-1].count("C") == 1 and len(set(s.upper()) & set(s)) == 2:
  print("AC")
else:
  print("WA")