n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
if sum(a) < sum(b):
    print(-1)
    exit()
s = 0
num = []
ok = True
for i in range(n):
    if a[i] < b[i]:
        s += b[i] - a[i]
        ans += 1
        ok = False
    else:
        num.append(a[i]-b[i])
if ok:
    print(0)
    exit()
num.sort()
t = 0
while s > t:
    t += num.pop()
    ans += 1

print(ans)
