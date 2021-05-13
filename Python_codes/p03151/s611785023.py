n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
s = 0
t = []
for i in range(n):
    if a[i] >= b[i]:
        t.append(a[i]-b[i])
    else:
        ans += 1
        s += b[i] - a[i]
m = len(t)
t.sort(reverse=True)
j = 0
while s > 0 and j < m:
    s -= t[j]
    j += 1
if s > 0:
    print(-1)
else:
    print(ans + j)