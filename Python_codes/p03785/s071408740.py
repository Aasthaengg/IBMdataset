N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

# パラメタの初期化
now = 0
now_f = 1
p = 0
cnt = 0

for t in T:
    # nowの更新
    if now_f == 1:
        now_f = 0
        now = t

    if t <= now + K:
        p += 1
        if p == C:
            p = 0
            cnt += 1
            now_f = 1

    else:
        p = 1
        cnt += 1
        now = t
        now_f = 0


if p == 0:
    print(cnt)
else:
    print(cnt + 1)
