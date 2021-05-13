n,m = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))
ans = 0
for i in range(2**n):
    lights = [0]*m
    onoff = [0]*n
    for j in range(n):
        if (i >> j) &  1:
            onoff[j] = 1
    for k in range(m):
        cnt = 0
        for l in s[k][1:]:
            if onoff[l-1] == 1:
                cnt += 1
        if cnt % 2 == p[k]:
            lights[k] = 1
    if all(g == 1 for g in lights):
        ans += 1
print(ans)

    
        


