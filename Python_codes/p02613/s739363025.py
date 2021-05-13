N = int(input())
ac, wa, tle, re = 0, 0, 0, 0
for i in range(N):
    result = input()
    if result == 'AC':
        ac += 1
    elif result == 'WA':
        wa += 1
    elif result == 'TLE':
        tle += 1
    else:
        re += 1
print('AC x %d\nWA x %d\nTLE x %d\nRE x %d' % (ac, wa, tle, re))