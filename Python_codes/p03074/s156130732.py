n, k = map(int, input().split())
s = input()
u = []
d = []
if s[0]=='0':
    d.append(0)
cnt = 1
for i in range(n-1):
    if s[i+1]=='1' and s[i]=='0':
        u.append(cnt)
        cnt = 1
    elif s[i+1]=='0' and s[i]=='1':
        d.append(cnt)
        cnt = 1
    else:
        cnt += 1
if s[-1]=='0':
    u.append(cnt)
    d.append(0)
else:
    d.append(cnt)
if len(u)<=k:
    print(n)
    exit()
tmp = sum(d[:k+1]) + sum(u[:k])
ans = tmp
for i in range(len(u)-k):
    tmp += u[i+k]+d[i+k+1]-u[i]-d[i]
    ans = max(ans, tmp)
print(ans)    