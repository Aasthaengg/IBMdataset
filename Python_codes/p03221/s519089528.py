from collections import defaultdict
n, m = map(int, input().split())
order = []
dd = defaultdict(int)

for i in range(m):
    p, y = map(int, input().split())
    order.append([i, p, y])

# 全体を年代順にソート
order.sort(key=lambda x: (x[2]))
# print(order)

ans = ['']*m
for ii, pp, yy in order:
    dd[pp] += 1
    ans[ii] = '{:0>6}{:0>6}'.format(pp, dd[pp])

print('\n'.join(ans))
