s = list(input())
l = list("CODEFESTIVAL2016")
ans = 0
for i in range(16):
    if s[i] != l[i]:
        ans += 1
print(ans)