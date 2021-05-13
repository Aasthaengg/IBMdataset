n = int(input())
a = list(map(int,input().split()))

ans = float('inf')
for _ in range(2):
    tmp = 0
    if _:
        if a[0] > 0:
            x = a[0]
        else:
            x = 1
            tmp = 1 - a[0]
    else:
        if a[0] < 0:
            x = a[0]
        else:
            x = -1
            tmp = 1 + a[0]
    for i in range(1, n):
        y = x + a[i]
        if x*y >= 0:
            if x > 0:
                tmp += y+1
                y -= y+1
            elif x < 0:
                tmp -= y-1
                y -= y-1
        x = y
    ans = min(ans, tmp)
print(ans)