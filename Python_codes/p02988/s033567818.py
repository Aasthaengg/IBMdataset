n = int(input())
P = list(map(int, input().split()))
ans = 0

for p1, p2, p3 in zip(P, P[1:], P[2:]):
    p = [p1, p2, p3]
    p.sort()
    if p2 == p[1]:
        ans += 1
print(ans)
