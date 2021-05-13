# B - Judge Status Summary

n = int(input())

AC = 0
WA = 0
TLE = 0
RE = 0

for i in range(n):
    j =input()
    if j == 'AC':
        AC += 1
    elif j == 'WA':
        WA += 1
    elif j == 'TLE':
        TLE += 1
    elif j == 'RE':
        RE += 1
print('''
AC x {}
WA x {}
TLE x {}
RE x {}
'''.format(AC,WA,TLE,RE))

