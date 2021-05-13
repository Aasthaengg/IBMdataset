n, m = map(int, input().split())
light = []
for i in range(m):
    tmp = list(map(int, input().split()))
    light.append(tmp[1:])
p = list(map(int, input().split()))
ans = 0
# 0 off, 1 on, bit全探索
for mask in range(1 << n):
    # print(mask)
    out = False
    # それぞれの電球について見る
    for i in range(len(light)):
        cnt = 0
        # 各電球が点くかを見たい
        for check in light[i]:
            if mask >> (check - 1) & 1:
                cnt += 1
        if cnt % 2 != p[i]:
            out = True
            break
    if not out:
        ans += 1

print(ans)
