s = list(input())
l = len(s)
ans = "NO"
for i in range(l):
    for j in range(1, l):
        t = s.copy()
        del t[i:j]
        if t == ["k","e","y","e","n","c","e"]:
            ans = "YES"
            break
print(ans)