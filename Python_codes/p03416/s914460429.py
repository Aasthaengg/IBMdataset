a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    s = str(i)
    f = True
    for j in range(len(s) // 2):
        if s[j] != s[-j-1]:
            f = False
            break
    if f:
        ans += 1
print(ans)