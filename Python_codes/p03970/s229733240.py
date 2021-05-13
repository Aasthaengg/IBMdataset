s = list(input())
t = list("CODEFESTIVAL2016")
ans = 0
for i in range(16):
    if not s[i] == t[i]:
        ans += 1
print(ans)