n, t = map(int,input().split())

lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))

ans = 1001001001
for i in lis:
    if i[1] <= t:
        ans = min(ans, i[0])
        

if ans == 1001001001:
    print("TLE")
else:
    print(ans)