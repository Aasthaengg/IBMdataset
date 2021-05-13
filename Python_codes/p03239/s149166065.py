n,T= map(int,input().split())
min = 1001
for i in range(n):
    c,t = map(int,input().split())
    if T >= t and min > c:
        min = c
if min > 1000:
    print('TLE')
else:
    print(min)