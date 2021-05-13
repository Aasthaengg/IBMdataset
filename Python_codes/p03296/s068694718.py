n = int(input())
a = list(map(int, input().split()))
ans = 0
c, s = 0, a[0]
for i in a:
    if i == s:
        c += 1
    else:
        ans += c // 2
        s = i
        c = 1
ans += c // 2
print(ans)