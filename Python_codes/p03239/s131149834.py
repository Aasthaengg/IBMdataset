n,t = map(int,input().split())

ans = 100000000000000
for i in range(n):
    x, y = map(int,input().split())
    if y > t:
        continue
    else:
        if ans > x:
            ans = x


if ans ==100000000000000:
    print("TLE")
else:
    print(ans)