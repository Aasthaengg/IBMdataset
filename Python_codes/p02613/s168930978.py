n = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for i in range(n):
  status = input()
  if status == 'AC':
    ac += 1
  elif status == 'WA':
    wa += 1
  elif status == 'TLE':
    tle += 1
  else:
    re += 1

print('AC x', ac)
print('WA x', wa)
print('TLE x', tle)
print('RE x', re)