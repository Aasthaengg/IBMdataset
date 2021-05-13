n = int(input())
a = []
for i in range(2):
    a.append(list(map(int, input().split(" "))))

ans_l = []
for i in range(n):
    ans = 0
    f = False
    for j in range(n):
        if j == 0:
            ans += a[0][0]
        elif f:
            ans += a[1][j]
        else:
            ans += a[0][j]

        if i == j:
            ans += a[1][j]
            f = True

    ans_l.append(ans)
print(max(ans_l))
