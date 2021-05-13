N = int(input())
cntAB = 0
cntA = 0
cntB = 0
BcntA = 0
for i in range(N):
  s = input()
  if s[0] == "B" and s[-1] == "A":
    BcntA += 1
  elif s[0] == "B" and s[-1] != "A":
    cntB += 1
  elif s[0] != "B" and s[-1] == "A":
    cntA += 1
  for j in range(1,len(s)):
    if s[j-1] == "A" and s[j] == "B":
      cntAB += 1
if BcntA!=0:
  if cntA+cntB>0:
    print(cntAB+min(cntA,cntB)+BcntA)
  else:
    print(cntAB+BcntA-1)
else:  
  print(cntAB+min(cntA,cntB))