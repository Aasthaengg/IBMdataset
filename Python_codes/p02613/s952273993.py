n=int(input())
k=[]
for i in(range(n)):
  k.append(str(input()))
ac=k.count('AC')
wa=k.count('WA')
tle=k.count('TLE')
re=k.count('RE')
print('AC x',ac)
print('WA x',wa)
print('TLE x',tle)
print('RE x',re)