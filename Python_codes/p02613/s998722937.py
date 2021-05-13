N = int(input())

AC, WA, TLE, RE = 0, 0, 0, 0

for i in range(N):
    S = input()
    if S == 'AC':
        AC += 1
    elif S == 'WA':
        WA += 1
    elif S == 'TLE':
        TLE += 1
    elif S == 'RE':
        RE += 1

print('AC x ' + str(AC))
print('WA x ' + str(WA))
print('TLE x ' + str(TLE))
print('RE x ' + str(RE))
