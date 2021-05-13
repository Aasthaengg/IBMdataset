n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
t = []
ans = 0
for i in range(n):
    if a[i] < b[i]:
        c += b[i] - a[i]
        ans += 1
    else:
        t.append(a[i]-b[i])
t.sort(reverse=True)
i = 0
while c > 0 and i < len(t):
    ans += 1
    c -= t[i]
    i += 1
if c > 0:
    print(-1)
else:
    print(ans)