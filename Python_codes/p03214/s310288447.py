N = int(input())
a = list(map(int, input().split()))
ave = sum(a)/N
ans = -1
now = 10000000000
for i in range(N):
  if abs(a[i]-ave) < now:
    ans = i
    now = abs(a[i]-ave)
print(ans)