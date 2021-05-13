N = int(input())
A = list(map(int, input().split()))
A.sort(reverse = True)
ans = 0
f = 0
for a in A:
  if f == 0:
    ans += a
  else:
    ans -= a
  f ^= 1
print(ans)