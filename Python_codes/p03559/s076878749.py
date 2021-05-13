import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

res = 0
for i in range(n):
    index1 = bisect.bisect_left(a, b[i])
    index2 = bisect.bisect_right(c, b[i])
    res += index1 * (n - index2)

print(res)
