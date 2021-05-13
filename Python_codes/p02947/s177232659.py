n = int(input())
s = [''.join(sorted(input())) for _ in range(n)]
ans = 0
d = {}
for i in s:
    if i in d:
        ans += d[i]
        d[i] += 1
    else:
        d[i] = 1
print(ans)