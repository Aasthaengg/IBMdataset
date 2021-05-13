from bisect import bisect_left, bisect_right
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    x = b[i]
    l = bisect_left(a, x)
    r = bisect_right(c, x)
    ans += l * (n - r)
print(ans)
