K = int(input())
A = list(map(int, input().split()))

# 最後に2人以上残るような最小のNを探す
ok, ng = 10 ** 18, 0
while abs(ok - ng) > 1:
    n = (ok + ng) // 2
    x = n
    for a in A:
        x = (x // a) * a
    if x >= 2:
        ok = n
    else:
        ng = n
m = ok

# 最後に2人以下になるような最大のNを探す
ok, ng = 0, 10 ** 18
while abs(ok - ng) > 1:
    x = (ok + ng) // 2
    n = x
    for a in A:
        x = x // a * a

    if x <= 2:
        ok = n
    else:
        ng = n
M = ok


# 条件を満たすかチェック
mx, Mx = m, M
for a in A:
    mx = (mx // a) * a
    Mx = (Mx // a) * a

if mx == 2 and Mx == 2:
    print(m, M)
else:
    print(-1)
