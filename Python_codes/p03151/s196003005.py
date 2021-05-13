n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split())) 
d = []

for i in range(n):
    d.append(a[i]-b[i])
d.sort()

sl = 0
ans = 0
for di in d:
    if di < 0:
        sl += di
        ans += 1
    else:
        break

if sl == 0:
    print(0)
    exit()

sr = 0
for di in reversed(d):
    if di >= 0 and sr +sl < 0:
        sr += di
        ans += 1

if sr + sl >= 0:
    print(ans)
else:
    print(-1)
