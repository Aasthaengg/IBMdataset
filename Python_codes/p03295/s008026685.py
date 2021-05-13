n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
ab.sort(key=lambda x: x[1])


s = ab[0][0]
e = ab[0][1]
ans = 1

for i in range(m):
    if (ab[i][0] <= s and e <= ab[i][1]) or s < ab[i][0] < e or s < ab[i][1] < e:
        continue

    ans += 1
    s = ab[i][0]
    e = ab[i][1]

print(ans)
