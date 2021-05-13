s = input()
if "C" in s and "F" in s and s.find("C") < s.rfind("F"):
  print("Yes")
else:
  print("No")