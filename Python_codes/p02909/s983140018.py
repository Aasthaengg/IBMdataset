from sys import stdin

s = stdin.readline().rstrip()

if s == 'Sunny':
    ans = 'Cloudy'
elif s == 'Cloudy':
    ans = 'Rainy'
else:
    ans = 'Sunny'

print(ans)