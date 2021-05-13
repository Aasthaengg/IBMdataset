n = int(input())
s = list(input())
ans = 0
for i in range(n - 1):
    sl = set(s[: i + 1])
    sr = set(s[i + 1 :])
    common = len(sl & sr)
    ans = max(common, ans)
print(ans)
