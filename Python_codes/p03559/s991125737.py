import bisect
n = int(input())
a = [sorted(list(map(int, input().split())))for _ in range(3)]
ans = 0
for b in a[1]:
  ans += bisect.bisect_left(a[0], b) * (n - bisect.bisect_right(a[2], b))
print(ans)