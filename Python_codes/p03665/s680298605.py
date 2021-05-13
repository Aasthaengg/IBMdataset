n, p = map(int, input().split())
A = list(map(int, input().split()))

check = all(a%2 == 0 for a in A)
ans = 0
if check and p == 0:
  ans = 1 << n
if not check:
  ans = 1 << (n-1)
print(ans)