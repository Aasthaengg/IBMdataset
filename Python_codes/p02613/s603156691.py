N = int(input())

result = [input().rstrip() for _ in range(N)]
print('AC x '+str(result.count('AC')))
print('WA x '+str(result.count('WA')))
print('TLE x '+str(result.count('TLE')))
print('RE x '+str(result.count('RE')))