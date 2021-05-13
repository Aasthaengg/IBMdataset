import sys


s = sys.stdin.readline().split('/')
if int(s[0]) < 2019:
    ans = 'Heisei'
if int(s[0]) == 2019 and int(s[1]) <= 4:
    ans = 'Heisei'
else:
    ans = 'TBD'
print(ans)
