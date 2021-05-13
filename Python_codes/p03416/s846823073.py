a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    s = str(i)
    flag = False
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag = True
    if not flag:
        ans += 1
print(ans)
