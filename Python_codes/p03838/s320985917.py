x, y = map(int, input().split())
minusx = x * -1
minusy = y * -1
a = [0]*4
a[0] = y - x
a[1] = y - minusx + 1
a[2] = minusy - x + 1
a[3] = minusy - minusx + 2
ans = 1001001001
for i in a:
    if i < 0:
        pass
    else:
        ans = min(ans,i)

print(ans)
