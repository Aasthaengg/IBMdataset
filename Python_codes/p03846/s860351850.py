n = int(input())
A = list(map(int, input().split()))
A.sort()
MOD = 10 ** 9 + 7
ans = 0
if n % 2 != 0:
  a = list(range(0, n, 2))
  a = sorted(a + a[1:])
  if a == A: ans = (2**((n-1)//2))%MOD
else:
  a = sorted(list(range(1, n, 2)) * 2)
  if a == A: ans = 2**(n//2)%MOD
print(ans)