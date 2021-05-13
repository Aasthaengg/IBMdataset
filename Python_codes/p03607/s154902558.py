n = int(input())
l = {}
ans = 0
for _ in range(n):
    a = int(input())
    if a in l:
        l[a] += 1
    else:
        l[a] = 1
for v in l.values():
    if v % 2 == 1:
        ans += 1
print(ans)