import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
num, ans, val = 0, 0, 0
vals = []

for i in range(n):
    c = b[i]-a[i]
    if c > 0:
        num += c
        ans += 1
    elif c < 0:
        vals.append(-c)
vals.sort()

if sum(a) < sum(b):
    print(-1)
else:
    for i in vals[::-1]:
        if val >= num:
            break
        ans += 1
        val += i
    print(ans)
