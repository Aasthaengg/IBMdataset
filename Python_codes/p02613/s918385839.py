n = int(input())
l = [input() for _ in range(n)]
print('AC x ' + str(l.count('AC')))
print('WA x ' + str(l.count('WA')))
print('TLE x ' + str(l.count('TLE')))
print('RE x ' + str(l.count('RE')))