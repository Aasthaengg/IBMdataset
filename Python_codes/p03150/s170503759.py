s = list(input())
key = list("keyence")
index = 0
ans = "NO"
n = len(s)
for i in range(8):
    mid = n-7
    tmp = s[:i] + s[i+mid:]
    if tmp == key:
        ans = "YES"
print(ans)