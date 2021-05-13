n = int(input())-2
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = a[0]
now = 1
cnt = 0
while n > 0:
    if cnt == 0:
        ans += a[now]
        cnt += 1
        n -= 1
    else:
        ans += a[now]
        cnt = 0
        n -= 1
        now += 1
print(ans)