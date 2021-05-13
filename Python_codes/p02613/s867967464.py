N = int(input())

S = []
for _ in range(N):
    s = input()
    S.append(s)

print('AC x {}'.format(S.count('AC')))
print('WA x {}'.format(S.count('WA')))
print('TLE x {}'.format(S.count('TLE')))
print('RE x {}'.format(S.count('RE')))