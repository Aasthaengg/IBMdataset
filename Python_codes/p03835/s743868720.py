k,s = map(int,input().split())
ans = 0
for i in range(k+1):
    for j in range(k+1):
        dum = (s - (i + j))
        if dum < 0:
            continue
        if dum <= k:
            ans += 1
print(ans)