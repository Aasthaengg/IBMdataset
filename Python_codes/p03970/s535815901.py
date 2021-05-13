s = list(input())
cf = "CODEFESTIVAL2016"
ans = 0
for i in range(16):
    if s[i] != cf[i]:
        ans += 1
print(ans)