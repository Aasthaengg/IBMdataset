N = int(input())

AC = []
WA = []
TLE = []
RE = []
for i in range(N):
  inp = input()
  if inp == "AC":
  	AC.append(1)
  elif inp == "WA":
    WA.append(1)
  elif inp == "TLE":
    TLE.append(1)
  elif inp == "RE":
    RE.append(1)
  
  
print ("AC x {}".format(len(AC)))
print ("WA x {}".format(len(WA)))
print ("TLE x {}".format(len(TLE)))
print ("RE x {}".format(len(RE)))