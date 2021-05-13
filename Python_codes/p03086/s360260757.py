s = list(input())
a = ["A", "C", "G", "T"]
ans = 0
l = []
for i in s:
    if i in a:
        ans += 1
        l.append(ans)
    else:
        ans = 0
        l.append(ans)
print(max(l))