from collections import Counter

N = int(input())
res = Counter([input() for _ in range(N)])

print('AC x ' + str(res['AC']))
print('WA x ' + str(res['WA']))
print('TLE x ' + str(res['TLE']))
print('RE x ' + str(res['RE']))
