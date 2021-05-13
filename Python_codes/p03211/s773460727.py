s = input()
n = len(s)

ans = 10000
for i in range(n-2):
    sbstr = s[i:i+3]
    val = abs(753 - int(sbstr))
    if val < ans:
        ans = val

print(ans)