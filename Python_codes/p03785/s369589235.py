n, c, k = map(int, input().split())
T = sorted([int(input()) for _ in range(n)])
ans = 1
first = T[0]
pas = 0
for t in T:
    pas += 1
    if t > first + k or pas > c:
        ans += 1
        pas = 1
        first = t
print(ans)