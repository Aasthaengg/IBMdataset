n = int(input())
d = [input() for i in range(n)]
ac = 0
wa = 0
tle = 0
re = 0

for i in range(n):
  if d[i] == 'AC':
    ac = ac + 1
  elif d[i] == 'WA':
    wa = wa +1
  elif d[i] == 'TLE':
    tle = tle +1
  else:
    re = re +1

print("AC x ",ac)
print("WA x ",wa)
print("TLE x ",tle)
print("RE x ",re)