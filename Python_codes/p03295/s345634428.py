n,m = map(int,input().split())
y = [list(map(int,input().split())) for _ in range(m)]
y.sort(key=lambda x:x[1])
s = y[0][1]-0.5
ans = 1
for i in range(1,m):
    a,b = y[i]
    if a < s < b:
        continue
    else:
        ans += 1
        s = b-0.5
print(ans)