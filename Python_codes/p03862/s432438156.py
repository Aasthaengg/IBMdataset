n, x = map(int, input().split())
a = list(map(int, input().split()))+[0]
ans = 0
for i in range(n):
    if a[i+1] + a[i] <= x:
        continue
    else:
        ans += (a[i+1] + a[i] - x)
        a[i+1] = max(0, x - a[i])
        # print(ans)
        # print(a)
print(ans)