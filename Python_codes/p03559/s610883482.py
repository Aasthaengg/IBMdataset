import bisect


n = int(input())
a =list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()
ans = 0
for i in range(n):
    num = b[i]
    x = bisect.bisect_left(a, num)
    y = bisect.bisect_right(c, num)
    ans += x * (n - y)

print(ans)