n,c,k = map(int,input().split())
buf = []
for i in range(n):
    t = int(input())
    buf.append(t)

buf.sort()

ans = 0
lasttime = 1e9
tcnt = 0
for i in range(n):
    if i == 0:
        tcnt += 1
        lasttime = buf[i]
        ans += 1
    else:
        t = buf[i]
        if t <= lasttime+k and tcnt < c:
            tcnt += 1
        else:
            ans += 1
            lasttime = buf[i]
            tcnt = 1
    # print(ans)
print(ans)