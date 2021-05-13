l = sorted(list(map(int,input().split())))
z = l[0]
y = l[1]
x = l[2]
# x > y > z

ans = 0

if (y-z) % 2 == 0:
    ans += (y-z)//2
    ans += (x-y)
else:
    x += 1
    z += 1
    ans += 1
    ans += (y-z)//2
    ans += (x-y)
print(ans)