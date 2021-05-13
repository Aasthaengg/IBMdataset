s = input()
t = input()
n = len(s)
m = len(t)
ans = m
for i in range(n-m+1):
    p = 0
    for j in range(m):
        if s[i+j] != t[j]:
            p += 1
    ans = min(ans,p)
print(ans)