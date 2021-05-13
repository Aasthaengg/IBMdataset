n = int(input())
a = list(map(int, input().split()))

ans = 1000
for i in a:
    x = 0
    while i:
        if i & 1:
            break
        else:
            x += 1
        i >>= 1
    ans = min(ans, x)
print(ans)