from operator import itemgetter
n, m = map(int, input().split())
l  = [list(map(int, input().split())) for i in range(m)]
l_sort = sorted(l, key=itemgetter(1))
ans = 0
last = 0
for i in range(m):
    if last <= l_sort[i][0]:
        last = l_sort[i][1]
        ans += 1
print(ans)
