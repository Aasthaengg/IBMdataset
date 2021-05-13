n,c,k = map(int,input().split())
t = [int(input()) for i in range(n)]+[float("INF")]
t.sort()
now = 0
count = 0
ans = 0
for i in t:
    if now == 0:
        now = i
        count += 1
    else:
        if i <= now+k:
            if count < c:
                count += 1
            else:
                ans += 1
                now = i
                count = 1
        else:
            ans += 1
            now = i
            count = 1
print(ans)