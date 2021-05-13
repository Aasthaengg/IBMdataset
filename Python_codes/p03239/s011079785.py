n,t = map(int, input().split())
ct = [ list(map(int,input().split(" "))) for i in range(n)]
ct.sort()
ans = 0
for i in range(n):
    if ct[i][1] <= t:
        ans = ct[i][0]
        break
if ans > 0:
    print(ans)
else:
    print('TLE')
