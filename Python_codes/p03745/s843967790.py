n = int(input())
a = list(map(int, input().split()))

up = down = 0

cur = a[0]
ans = 0
for x in a:
    if cur < x:
        up = 1
    elif cur > x:
        down = 1
    
    if up and down:
        ans += 1
        up = down = 0

    cur = x

print(ans+1)