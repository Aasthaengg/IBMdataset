s=input()
AC="AC"
if not s[0]=="A":
  AC="WA"
s=s[1:]  
if not s[1:-1].count("C")==1:
  AC="WA"
s=s.replace("C","c")


if not s.islower():
  AC="WA"
  
print(AC)