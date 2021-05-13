n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)

ac = wa = re = tle = 0
for i in range(n):
    if s[i] == 'AC':
        ac += 1
    elif s[i] == 'WA':
        wa += 1
    elif s[i] == 'RE':
        re += 1
    else:
        tle += 1

print(f'AC x {ac}')
print(f'WA x {wa}')
print(f'TLE x {tle}')
print(f'RE x {re}')