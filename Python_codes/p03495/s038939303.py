import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = collections.Counter(a)
ans = 0
t=cnt.most_common()
if len(t) <= k:
    print(0)
    exit()

for i in range(k):
    ans += t[i][1]
print(n - ans)