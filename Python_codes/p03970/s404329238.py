s = input()
ans = 0
s2 = "CODEFESTIVAL2016"
n = len(s)
for i in range(n):
    if s[i] != s2[i]:
        ans += 1
print(ans)
