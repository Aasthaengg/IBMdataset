S = input()
N = len(S)

# RR...RLL...L　の形に分割したい
# 境界は"LR"となっているはず

# "LR"の"L"のindexを記録
boundary = []
for i in range(N - 1):
    if S[i] == "L" and S[i + 1] == "R":
        boundary.append(i)

# boundary は R..RL..Lの左端 として扱いたいので、N-1も追加
boundary.append(N - 1)

ans = [0] * N

l = 0
for r in boundary:
    mid = 0
    # [indexが偶数の個数, indexが奇数の個数]
    cnt = [0, 0]
    for x in range(l, r + 1):
        cnt[x % 2] += 1
        # R...RL...Lの"RL"の位置を探す
        # "RL"の"R"のindexをmidに代入
        if x < r and S[x] == "R" and S[x + 1] == "L":
            mid = x

    # 十分な操作をすると、indexの偶奇で[mid]か[mid+1]のどちらかに集まる
    # midが偶数の場合
    if mid % 2 == 0:
        ans[mid] = cnt[0]
        ans[mid + 1] = cnt[1]
    # midが奇数の場合
    elif mid % 2 == 1:
        ans[mid] = cnt[1]
        ans[mid + 1] = cnt[0]

    # 次の区間の左端 = 今の区間の右端 + 1
    l = r + 1

print(*ans)
