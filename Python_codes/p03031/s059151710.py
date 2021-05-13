n, m = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for i in range(1 << n):
    tmp = 0
    for j in range(m):
        on = 0
        for k in range(1, s[j][0]+1):
            if i & (1 << s[j][k]-1):
                on += 1
        if p[j] % 2 == on % 2:
            tmp += 1
    if tmp == m:
        ans += 1

print(ans)
