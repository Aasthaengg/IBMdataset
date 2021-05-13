n,t = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]
ans = 10000
for i in range(n):
    if ct[i][1] <=t:
        tmp = ct[i][0]
        ans = min(ans, tmp)
print(ans if ans != 10000 else 'TLE')