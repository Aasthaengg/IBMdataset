n, m = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for bit in range(1 << 3):
    b = []
    for i in range(n):
        tmp = 0
        for j in range(3):
            if bit & (1 << j):
                tmp += cakes[i][j]
            else:
                tmp -= cakes[i][j]
        b.append(tmp)
    b.sort(reverse=True)
    ans = max(ans, sum(b[:m]))
print(ans)