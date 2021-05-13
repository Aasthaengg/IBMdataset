n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
p = sorted(p, reverse = True)
ans = 0
for i in range(n):
    if i == 0: ans += p[i] // 2
    else: ans += p[i]
print(ans)