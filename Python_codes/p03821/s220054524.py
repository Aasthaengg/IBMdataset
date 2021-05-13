n = int(input())
ll = [list(map(int, input().split())) for _ in range(n)]

ll = ll[::-1]

ans = 0
res = 0
sub = 0

for a, b in ll:
    if (a + ans) % b == 0:
        continue
    res = (a + ans) % b
    sub = b - res

    ans += sub

print(ans)