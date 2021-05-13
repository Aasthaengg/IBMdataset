import collections
n = int(input())
a = list(map(int, input().split()))
a = collections.Counter(a)
ans = []
for i, j in a.items():
    if j >= 2:
        for _ in range(j):
            ans.append(i)
ans.sort(reverse=True)
if len(ans) <= 3:
    print(0)
else:
    print(ans[0]*ans[3])