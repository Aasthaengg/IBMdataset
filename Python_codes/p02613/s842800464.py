Judge = [0,0,0,0]
n = int(input())
S = [input() for i in range(n)]

print('AC x',S.count('AC'))
print('WA x',S.count('WA'))
print('TLE x',S.count('TLE'))
print('RE x',S.count('RE'))