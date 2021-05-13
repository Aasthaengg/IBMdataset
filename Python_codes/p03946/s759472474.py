from collections import Counter
n, t = map(int, input().split())
a = list(map(int, input().split()))
cnt = Counter(a)
cnt_tmp = Counter()
#i番目以下の最小値
min_a = [a[0] for _ in range(n)]
for i in range(n-1):
    min_a[i+1] = min(a[i+1], min_a[i])

res = 0
for i in range(1, n):
    res = max(a[i] - min_a[i-1], res)

ans = 0
for i in range(n):
    cnt_tmp[a[i]] += 1
    x = a[i] + res
    cnt_a = cnt_tmp[a[i]]
    cnt_x = cnt[x] - cnt_tmp[x]
    ans += min(cnt_a, cnt_x)

print(ans)
