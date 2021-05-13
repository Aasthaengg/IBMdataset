n = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for i in range(n):
  k = input().upper()
  if k == 'AC':
    ac +=1
  elif k == 'WA':
    wa +=1
  elif k == 'TLE':
    tle +=1
  elif k == 'RE':
    re +=1
    
print('{} x {}'.format('AC',ac))
print('{} x {}'.format('WA',wa))
print('{} x {}'.format('TLE',tle))
print('{} x {}'.format('RE',re))