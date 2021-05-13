import sys
S = input()
if S[0] != "A":
  print("WA")
  sys.exit()

if S[1:].count('C') != 1:
  print("WA")
  sys.exit()

Cindex = S.find("C")
if Cindex < 2 or Cindex > len(S)-2:
  print("WA")
  sys.exit()
  
T = 'a' + S[1:]
T = T[0:Cindex] + "c" + T[Cindex+1:]

if T.islower():
  print("AC")
else:
  print("WA")