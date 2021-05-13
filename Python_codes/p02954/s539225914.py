s = input()
n = len(s)

boundary = []
ans = [0] * n
# "LR"を記録、Lの方のindexをboundaryにappend
for i in range(n - 1):
    if s[i] == "L" and s[i + 1] == "R":
        boundary.append(i)

# n-1があると後のfor文で都合が良いので足しておく
boundary.append(n - 1)
# RR...RLL...L　の形に分割されている

l = 0
for r in boundary:
    middle = 0
    cnt = [0, 0]
    for x in range(l, r + 1):
        # xが偶数ならcnt[0], 奇数ならcnt[1]をincrement
        cnt[x % 2] += 1
        # "RL"を記録、Rの方のindexをmiddleに代入
        if x < r and s[x] == "R" and s[x + 1] == "L":
            middle = x

    # indexが偶数のものが一か所に、奇数のものが別の一か所(左右隣り合う)に集約される
    # middleが偶数の時
    if middle % 2 == 0:
        ans[middle] = cnt[0]
        ans[middle + 1] = cnt[1]
    # middleが奇数の時
    elif middle % 2 == 1:
        ans[middle] = cnt[1]
        ans[middle + 1] = cnt[0]

    l = r + 1

print(*ans)
