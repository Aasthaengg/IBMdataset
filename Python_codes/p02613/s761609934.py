N=int(input())

AC=0
WA=0
TLE=0
RE=0

for i in range(N):
    j=input()
    if j=='AC': 
        AC+=1
    elif j=='WA':
        WA+=1
    elif j=='TLE':
        TLE+=1
    else:
        RE += 1

print('AC x {}'.format(AC))
print('WA x {}'.format(WA))
print('TLE x {}'.format(TLE))
print('RE x {}'.format(RE))