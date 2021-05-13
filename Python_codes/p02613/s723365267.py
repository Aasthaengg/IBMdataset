a, b, c, d =0, 0, 0 , 0
for i in range(int(input())):
    x = input()
    if x == 'AC':
        a += 1
    if x == 'TLE':
        b += 1
    if x == 'RE':
        c += 1
    if x == 'WA':
        d += 1
print('AC x', a)
print('WA x', d)
print('TLE x', b)
print('RE x', c)
