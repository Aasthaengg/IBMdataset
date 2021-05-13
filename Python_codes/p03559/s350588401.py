import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    tmp = 1
    x = bisect.bisect_left(a, b[i])
    y = bisect.bisect_right(c, b[i])
    ans += x*(n-y)
print(ans)