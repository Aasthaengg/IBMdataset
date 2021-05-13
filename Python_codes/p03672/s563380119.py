s = input()
n = len(s)
ans = 0
for i in range(1, n // 2):
    if s[:i] == s[i : 2 * i]:
        ans = max(ans, 2 * i)
print(ans)
