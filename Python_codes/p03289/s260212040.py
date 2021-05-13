import sys
S = list(input())
C_cnt,low,upp = 0,0,0
if S[0] != "A" or S[-1].isupper() or S[1].isupper():
  print("WA")
  sys.exit()
for i in range(2,len(S)-1):
  if S[i] == "C":
    C_cnt += 1
  elif S[i].islower():
    low += 1
  elif S[i].isupper():
    upp += 1
if C_cnt == 1 and low == len(S)-4 and upp == 0:
  print("AC")
else :
  print("WA")
