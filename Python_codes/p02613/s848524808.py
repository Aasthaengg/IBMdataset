N = int(input())

AC_counter = 0
WA_counter = 0
TLE_counter = 0
RE_counter = 0

for i in range(N):

    S = str(input())

    if S == 'AC':
        AC_counter += 1
    elif S == 'WA':
        WA_counter += 1
    elif S == 'TLE':
        TLE_counter += 1
    elif S == 'RE':
        RE_counter += 1


print('AC x ' + str(AC_counter))
print('WA x ' + str(WA_counter))
print('TLE x ' + str(TLE_counter))
print('RE x ' + str(RE_counter))
