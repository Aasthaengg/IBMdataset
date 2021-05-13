import re

s=input()

def isBoin(f):
  if f == "a" or f == "i" or f == "u" or f == "e" or f == "o":
    return True
  else:
    return False

n = s[0]
f = s[1]
if isBoin(n) == True:
  n += s[1]
  n += s[2]
else:
  n += s[1]
  n += s[2]
print(n)