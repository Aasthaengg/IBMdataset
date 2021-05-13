a, b = map(int, input().split())

res = 0
for v in range(a, b+1):
    s = str(v)
    if s[0] == s[4] and s[1] == s[3]:
        res += 1
print(res)