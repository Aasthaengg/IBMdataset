n = int(input())
a = [int(x) for x in input().split()]

dir = 0
old = a[0]
ans = 1
for i in range(1, len(a)):
    now = a[i]
    if dir == 0:
        if old < now:
            dir = 1
        elif old > now:
            dir = -1
    elif dir == 1:
        if old > now:
            dir = 0
            ans += 1
    elif dir == -1:
        if old < now:
            dir = 0
            ans += 1
    old = now
print(ans)

