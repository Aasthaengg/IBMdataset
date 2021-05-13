n,m = (int(x) for x in input().split())

sec = []

for i in range(m):
    list = [int(i) for i in input().split()]
    list.reverse()
    sec.append(list)

sec.sort()
left = sec[0][0]
right = sec[0][1]
x = right - 1
ans = 0

for i in range(m):
    if sec[i][1]<x:
        continue
    else:
        x = sec[i][0]
        ans += 1

print(ans)
