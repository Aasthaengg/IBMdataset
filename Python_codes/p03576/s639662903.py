N, K = map(int, input().split())
xys = [tuple(map(int, input().split())) for _ in range(N)]

# H - x - i
# W - y - j

xs_decode = sorted(map(lambda t: t[0], xys))
ys_decode = sorted(map(lambda t: t[1], xys))
xs_encode = {e:i for i, e in enumerate(xs_decode)}
ys_encode = {e:i for i, e in enumerate(ys_decode)}

H = len(xs_encode)
W = len(ys_encode)

field_csum = [[0] * (W+1) for _ in range(H+1)]
for x, y in xys:
    i = xs_encode[x]
    j = ys_encode[y]
    field_csum[i+1][j+1] += 1
for i in range(H+1):
    for j in range(W):
        field_csum[i][j+1] += field_csum[i][j]
for i in range(H):
    for j in range(W+1):
        field_csum[i+1][j] += field_csum[i][j]


ans = 1 << 63 # INF
# bi < i <= ei and bj < j <= ej
for bi in range(H):
    for ei in range(bi + 1, H + 1):
        for bj in range(W):
            for ej in range(bj + 1, W + 1):
                if field_csum[ei][ej] - field_csum[bi][ej] - field_csum[ei][bj] + field_csum[bi][bj] >= K:
                    area = (xs_decode[ei-1] - xs_decode[bi]) * (ys_decode[ej-1] - ys_decode[bj])
                    ans = min(ans, area)
                    break # don't have to check larger ej 

print(ans)