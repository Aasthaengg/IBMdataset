n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
ans = 1
passenger = 0
limit = t[0] + k
 
for p in t:
    if passenger < c and p <= limit:
        passenger += 1
    else:
        ans += 1
        passenger = 1
        limit = p + k
print(ans)