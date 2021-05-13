n = int(input())
ans_ac = 0
ans_wa = 0
ans_tle = 0
ans_re = 0

for i in range(n):
    s = input()
    if s == 'AC':
        ans_ac += 1
    elif s == 'WA':
        ans_wa += 1
    elif s == 'TLE':
        ans_tle += 1
    else:
        ans_re += 1
        
print('AC x '+str(ans_ac))
print('WA x '+str(ans_wa))
print('TLE x '+str(ans_tle))
print('RE x '+str(ans_re))
