H, W, A, B = map(int, input().split())
row = [A, W-A]
col = [B, H-B]
ans = ''
for i in [0, 1]:
    for y in range(col[i]):
        for j in [0, 1]:
            for x in range(row[j]):
                ans += str(j^i)
        ans +='\n'
print(ans)