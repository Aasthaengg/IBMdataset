import collections
A = input()
cnt = collections.defaultdict(int)
ans = 1
for i, a in enumerate(A):
    ans += i - cnt[a]
    cnt[a] += 1
print(ans)
