n = int(input())
p = list(map(int,input().split()))
i = 0
ans = 0
while i < len(p) - 3 + 1:
    m = p[i:i+3]
    l = sorted(m)
    if l[1] == m[1]:
        ans += 1
    i += 1
print(ans)