Num = int(input())
AC =0
WA =0
TLE=0
RE =0

for i in range(Num):
  s = input()
  if(s=='AC'):
    AC+=1
  if(s=='WA'):
    WA+=1
  if(s=='TLE'):
    TLE+=1
  if(s=='RE'):
    RE+=1
    
print('AC x '+str(AC))
print('WA x '+str(WA))
print('TLE x '+str(TLE))
print('RE x '+str(RE))
