ls = [[int(_) for _ in input().split()] for _ in range(3)]

cnt = [0] * 4

for i in range(3):
    for j in range(2):
        if ls[i][j] == 1:
            cnt[0] += 1
        elif ls[i][j] == 2:
            cnt[1] += 1
        elif ls[i][j] == 3:
            cnt[2] += 1
        elif ls[i][j] == 4:
            cnt[3] += 1

if min(cnt) == 0 or max(cnt) == 3:
    print("NO")
else:
    print("YES")