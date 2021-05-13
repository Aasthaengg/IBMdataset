n = int(input())
a = [int(i) for i in input().split()]
cnt = [0,0]
s = [0,0]
for i in range(n):
    s[0] += a[i]
    s[1] += a[i]
    if i%2 == 0:
        if s[0] <= 0:
            cnt[0] += -s[0]+1
            s[0] = 1
        if s[1] >= 0:
            cnt[1] += s[1]+1
            s[1] = -1
    else:
        if s[1] <= 0:
            cnt[1] += -s[1]+1
            s[1] = 1
        if s[0] >= 0:
            cnt[0] += s[0]+1
            s[0] = -1
ans = min(cnt)
print(ans)