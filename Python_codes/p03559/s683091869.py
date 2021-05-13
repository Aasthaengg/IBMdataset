import bisect
n = int(input())
a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])
c = sorted([int(i) for i in input().split()])
ans = 0
for i in b:
    ans += bisect.bisect_left(a, i) * (n - bisect.bisect(c, i))
print(ans)
