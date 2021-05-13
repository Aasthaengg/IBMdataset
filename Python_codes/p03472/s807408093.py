n, h = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab = sorted(ab, key=lambda ab: (-ab[0], ab[1]))  # aの大きいやつを取り出す
maxa = ab[0][0]
maxa_b = ab[0][1]
ab[0][0] = 0
ab[0][1] = 0
# print()
# print(maxa, maxa_b)

ab = sorted(ab, key=lambda ab: (-ab[1]))
# print(ab)
ans = 0
for i in range(n-1):
    if h <= 0:
        print(ans)
        break

    if h <= maxa_b:
        ans += 1
        print(ans)
        break

    if maxa < ab[i][1]:
        h -= ab[i][1]
        ans += 1
    else:
        h -= maxa
        ans += 1
    # print(h)
else:
    # print(h, ans, "SDFGH")
    ans += 1
    h -= maxa_b
    if h <= 0:
        print(ans)
    else:
        if h % maxa == 0:
            ans += h//maxa
        else:
            ans += h//maxa+1
        print(ans)
