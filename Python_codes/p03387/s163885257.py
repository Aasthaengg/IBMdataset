a = list(map(int , input().split()))
a.sort()
ans = 0
ans += ((a[-1]-a[0]) // 2)
ans += ((a[-1]-a[1]) // 2)
a[0] += 2 * ((a[-1]-a[0]) // 2)
a[1] += 2 * ((a[-1]-a[1]) // 2)
a.sort()
if a[0] < a[-1] and a[1] == a[-1]:
    print(ans + 2)
    exit()
if a[0] < a[-1] and a[1] < a[-1]:
    print(ans + 1)
    exit()
print(ans)
