n = int(input())

odds = [i for i in range(1, n+1, 1) if i%2 != 0]
cnt_lists = []
for j in odds:
    cnt = 0
    for k in range(1, j+1, 1):
        if j%k == 0:
            cnt += 1
    cnt_lists.append(cnt)

ans = cnt_lists.count(8)
print(ans)