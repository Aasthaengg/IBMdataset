from itertools import product
n, m = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(m)]
pl = list(map(int, input().split()))
ans = 0
for bits in product([0, 1], repeat=n):
    flag = True
    for i, ss in enumerate(s):
        cnt = 0
        for sss in ss[1:]:
            if bits[sss-1] == 1:
                cnt += 1
        if not cnt % 2 == pl[i]:
            flag = False
    if flag:
        ans += 1
print(ans)
