N = int(input())

c0 = 0
c1 = 0
c2 = 0
c3 = 0

for i in range(N):
    s = input()
    if s == 'AC':
        c0 += 1
    elif s == 'WA':
        c1 += 1
    elif s == 'TLE':
        c2 += 1
    elif s == 'RE':
        c3 += 1

print('AC x {}\nWA x {}\nTLE x {}\nRE x {}'.format(c0, c1, c2, c3))