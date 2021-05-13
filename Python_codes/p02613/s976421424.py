n=int(input())
ac=0
wa=0
tle=0
re=0
for m in range(n):
  a=input()
  if a=='AC':
    ac=ac+1
  elif a=='WA':
    wa=wa+1
  elif a=='TLE':
    tle=tle+1
  else:
    re=re+1
print('AC x '+str(ac))
print('WA x '+str(wa))
print('TLE x '+str(tle))
print('RE x '+str(re))