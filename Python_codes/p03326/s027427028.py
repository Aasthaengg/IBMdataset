n, m = map(int, input().split(" "))

xyz = list()
for i in range(0, n):
    x, y, z = map(int, input().split(" "))
    xyz.append((x, y, z))

ans = 0
for a1 in [1, -1]:
    for a2 in [1, -1]:
        for a3 in [1, -1]:
            tmp = list()
            for x, y, z in xyz:
                tmp.append(x * a1 + y * a2 + z * a3)

            sorted_calc = sorted(tmp, reverse=True)
            sum = 0
            for i in range(0, m):
                sum += sorted_calc[i]

            ans = max(sum, ans)

print(ans)
