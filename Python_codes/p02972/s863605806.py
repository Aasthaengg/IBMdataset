n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
m = 0
res = []
# 1 idx
for i in range(n, 0, -1):
    # i の倍数でbit立っているものの個数を数える
    cnt = 0
    idx = 2
    while i * idx <= n:
        if ans[i * idx - 1]:
            cnt += 1
        idx += 1
    debug = cnt
    if cnt % 2 != a[i - 1]:
        ans[i - 1] = 1
        m += 1
        res.append(i)
print(m)
if m:
    print(*res)
