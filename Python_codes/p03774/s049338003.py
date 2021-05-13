n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]

ans = []
for a, b in ab:
    mx, j = 10**20, 0
    for i in range(m):
        c, d = cd[i]
        l = abs(a-c) + abs(b-d)
        if l < mx: 
            j = i
            mx = l
    ans.append(j+1)

print('\n'.join(map(str, ans)))