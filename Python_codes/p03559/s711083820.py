n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

from bisect import bisect_left,bisect_right
ans = 0
for i in range(n):
    pos_a = bisect_left(a,b[i])
    pos_c = bisect_right(c,b[i])
    ans += pos_a*(n-pos_c)

print(ans)