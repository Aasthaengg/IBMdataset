n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]
ans = x
for i in range(n) :
    day = 1
    while day <= d :
        ans += 1
        day += a[i]
print(ans)
