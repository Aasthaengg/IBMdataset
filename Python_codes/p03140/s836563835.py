n = int(input())
l = [list(input()) for i in range(3)]
ans = 0
for i in range(n):
    s = set()
    for j in range(3):
        s.add(l[j][i])
    k = len(s)
    if k == 2:
        ans += 1
    elif k == 3:
        ans += 2
print(ans) 