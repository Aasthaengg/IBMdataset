s = input()
n = len(s)
s += "o"*(15-n)
if s.count("o") >= 8:
  print("YES")
else:
  print("NO")