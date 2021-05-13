import sys
input = sys.stdin.readline
n, d, a = map(int, input().split())
xh = sorted([tuple(map(int, input().split()))for _ in range(n)])
INF = 10**18
x_list = [x for x, h in xh]
x_list.append(INF)

end_idx_list = [0]*n
idx = 0
for i in range(n):
    while True:
        if x_list[i]+2*d < x_list[idx]:
            end_idx_list[i] = idx
            break
        idx += 1

damage = [0]*(n+1)
ans = 0
for i in range(n):
    x, h = xh[i]
    h -= damage[i]
    if 0 < h:
        cnt = -(-h//a)
        ans += cnt
        damage[i] += cnt*a
        end_idx = end_idx_list[i]
        damage[end_idx] -= cnt*a

    damage[i+1] += damage[i]
print(ans)
