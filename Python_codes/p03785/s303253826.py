n,c,k = map(int,input().split())
t = []
for i in range(n):
    t.append(int(input()))

t.sort()

ans = 0
cnt = 0
tmp = 0
s = t[0]

while tmp < n:
    t1 = t[tmp]
    cnt += 1
    if t1 - s > k:
        ans += 1
        cnt = 1
        s = t[tmp]
    elif cnt == c:
        if tmp < n - 1:
            s = t[tmp + 1]
            ans += 1
            cnt = 0

    tmp += 1

if cnt > 0:
    ans += 1

print(ans)
