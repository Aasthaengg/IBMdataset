n = int(input())
Sn = []

for i in range(n):
    Sn.append(input())

ac = Sn.count('AC')
wa = Sn.count('WA')
tle = Sn.count('TLE')
re = Sn.count('RE')

print('AC x {}'.format(ac))
print('WA x {}'.format(wa))
print('TLE x {}'.format(tle))
print('RE x {}'.format(re))