n, m = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(2**3):
    tmp_arr = []
    for j in range(n):
        tmp = 0
        for k in range(3):
            if (i>>k) & 1:
                tmp += cakes[j][k]
            else:
                tmp -= cakes[j][k]
        tmp_arr.append(tmp)
    tmp_arr.sort(reverse=True)
    ans = max(ans, sum(tmp_arr[:m]))
print(ans)