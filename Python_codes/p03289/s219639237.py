import sys
s = input()

answer = True
if s[0] != "A":
  answer = False

if s[2:len(s)-1].count("C") != 1:
  answer = False
  
for i in range(len(s)):
  if s[i] != "A" and s[i] != "C":
    if ord(s[i]) < 97  or  122 < ord(s[i]):
      answer = False

if answer :      
  print("AC")
else :
  print("WA")