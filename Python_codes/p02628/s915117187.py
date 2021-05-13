import collections
n, k = map(int, input().split())
p = list(map(int, input().split()))
selected = []
ans = 0
cnt = 0
choice = collections.defaultdict(int)
for i in range(len(p)):
    choice[p[i]] += 1
for v in sorted(choice.keys()):
    if cnt < k:
        if choice[v] > k - cnt:
            ans += v * k - cnt
            k -= k - cnt
        else:
            ans += v * choice[v]
            k -= choice[v]
print(ans)
