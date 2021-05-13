n, tt = map(int,input().split())
s = 1001
for i in range(n):
    c, t = map(int,input().split())
    if c < s and t <= tt:
        s = c
if s > 1000:
    print('TLE')
else:
    print(s)