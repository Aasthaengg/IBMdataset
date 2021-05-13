import re
S = input()
string = re.findall(r'([ACGT]+)', S)

if len(string) != 0:
  lenst = [len(x) for x in string]
  print(max(lenst))
  
else:
  print(0)