s = input()

if (s.find("C") != -1 ) and (s.rfind("F") !=-1) and(s.find("C") < s.rfind("F")):
  print("Yes")
else:
  print("No")