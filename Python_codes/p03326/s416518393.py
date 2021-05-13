N, M = map(int, input().split())
xyz = []
for _ in range(N):
    x, y, z = map(int, input().split())
    xyz.append((x, y, z))

ans = 0

# 綺麗さ、美味しさ、人気度について、
# 正の方向に最大化するか、負の方向に最大化するか
# 2*2*2 = 8通り

# ex. 正、正、負の場合
# x + y - z を計算してソートし、上からM個の総和を取る

for a in [-1, 1]:
    for b in [-1, 1]:
        for c in [-1, 1]:
            tmp = []
            for i in range(N):
                tmp.append(a * xyz[i][0] + b * xyz[i][1] + c * xyz[i][2])
            tmp.sort(reverse=True)

            tmp2 = sum(tmp[:M])
            ans = max(ans, tmp2)

print(ans)
