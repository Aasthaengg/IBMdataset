ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

ans = 0

for i in range(n):
  ans += a[i]-1

print(ans)