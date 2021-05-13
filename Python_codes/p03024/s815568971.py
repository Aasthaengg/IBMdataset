s = input()
nokori = 15 -len(s)
should = 8 -nokori 
num = s.count("o")
if num >= should:
  print("YES")
else:
  print("NO")