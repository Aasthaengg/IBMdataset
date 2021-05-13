n,c,k = map(int,input().split())
ls = [int(input()) for _ in range(n)]
ls.sort()
ans = 0
cnt = 0
l,r = 0,0
for i in range(n):
    if l == 0:
        l = ls[i]
        r = ls[i] + k
    cnt += 1
    if cnt == c:
        ans += 1
        cnt = 0
        l = 0
        continue
    if i != n-1:
        if ls[i+1] > r:
            ans += 1
            cnt = 0
            l = 0
            continue
if cnt > 0:
    ans += 1
print(ans)