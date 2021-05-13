n = int(input())
a = list(map(int, input().split(" ")))
a = sorted(a)[::-1]

if n % 2:
  ans = a[0] + 2 * sum(a[1:(n//2)]) + a[n//2]
else:
  ans = a[0] + 2 * sum(a[1:(n//2)])

print(ans)