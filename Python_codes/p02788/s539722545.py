n, d, a = map(int, input().split())
xh = []
for i in range(n):
    xi, hi = map(int, input().split())
    xh.append([xi, hi])

xh.sort(key=lambda x: x[0])
x, h = [], []
for i in range(n):
    x.append(xh[i][0])
    h.append(xh[i][1])

cnt = 0
dmg = [0 for i in range(n+1)]
for i in range(n):
    xi, hi = x[i], h[i]
    dmg[i] += dmg[i-1]
    hi -= dmg[i]
    if hi <= 0:
        continue
    else:
        num = (hi+a-1)//a
        cnt += num
    point = xi + 2*d
    left = i
    right = n
    while left+1 < right:
        mid = (left+right)//2
        if x[mid] <= point:
            left = mid
        else:
            right = mid
    dmg[i] += num*a
    dmg[left+1] -= num*a
print(cnt)