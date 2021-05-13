n = int(input())
results = [input() for i in range(n)]
ac = results.count('AC')
wa = results.count('WA')
tle = results.count('TLE')
re = results.count('RE')

print('AC','x',ac)
print('WA','x',wa)
print('TLE','x',tle)
print('RE','x',re)