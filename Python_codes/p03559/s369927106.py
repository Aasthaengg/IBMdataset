# ABC084C - Snuke Festival
from bisect import bisect_left, bisect_right

n = int(input())
lst_a = sorted(list(map(int, input().rstrip().split())))
lst_b = sorted(list(map(int, input().rstrip().split())))
lst_c = sorted(list(map(int, input().rstrip().split())))
lgth = len(lst_c)
ans = 0
for i in lst_b:
    ans += bisect_left(lst_a, i) * (lgth - bisect_right(lst_c, i))
print(ans)