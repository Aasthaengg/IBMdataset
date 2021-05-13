n = int(input())
s = [input()for i in range(n)]
c0 = 0
c1 = 0
c2 = 0
c3 = 0
for i in range(n):
    if s[i] == 'AC':
        c0 += 1
    elif s[i] == 'WA':
        c1 += 1
    elif s[i] == 'TLE':
        c2 += 1
    else:
        c3 += 1
print(f'AC x {c0}\nWA x {c1}\nTLE x {c2}\nRE x {c3}')

