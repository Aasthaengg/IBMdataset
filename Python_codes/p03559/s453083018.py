import bisect
a = int(input())
b = list(map(int, input().split()))
b.sort()
c = list(map(int, input().split()))
d = list(map(int, input().split()))
d.sort()
ans = 0
for i in range(a):
    ans += bisect.bisect_left(b, c[i]) * (a - bisect.bisect_right(d, c[i]))
print(ans)
