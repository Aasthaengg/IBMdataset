a,b,c = map(int,input().split())

x = max(a,b,c)
z = min(a,b,c)
y = a + b + c - x - z

cnt = 0

if z % 2 == y % 2:
    cnt += (y - z) / 2
    cnt += (x - y)
elif z % 2 != y % 2 and z % 2 == x % 2:
    cnt += (x - z) / 2
    if y % 2 == x % 2:
        cnt += (x - y)
    else:
        cnt += ((x + 1)- y) / 2
        cnt += 1
elif z % 2 != y % 2 and z % 2 != x % 2:
    cnt += (x - y) / 2
    cnt += ((x + 1)- z) / 2
    cnt += 1

print(int(cnt))