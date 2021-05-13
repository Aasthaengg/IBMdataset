n = int(input())
s = [input() for i in range(n)]
empl = [[],[],[],[]]
for i in s:
    if i == 'AC':
        empl[0].append(i)
    elif i == 'WA':
        empl[1].append(i)
    elif i == 'TLE':
        empl[2].append(i)
    else:
        empl[3].append(i)
print('AC x',len(empl[0]))
print('WA x',len(empl[1]))
print('TLE x',len(empl[2]))
print('RE x',len(empl[3]))