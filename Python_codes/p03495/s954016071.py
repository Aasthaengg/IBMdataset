import collections
N, K = map(int, input().split())
A_list = list(map(str,input().split()))

ans = 0
c = collections.Counter(A_list)
if K >= len(c):
    ans = 0
else:
    foo = len(c)-K
    bar_list = list(c.values())
    bar_list.sort()
    for i in range(foo):
        ans += bar_list[i]

print(ans)