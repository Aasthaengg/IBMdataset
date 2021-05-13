s = str(input())
num = 0

if s[0] == "A":
  if "C" in s[2:len(s)-1]:
    for i in s:
      if i.isupper():
        num += 1
    if num == 2:
      print("AC")
      exit(0)
      
print("WA")