from bisect import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
R = [0]
s = 0
for a in A:
  s = (s+a)%M
  R.append(s)
R.sort()
ans = 0
n = 1
x = R[0]
for r in R[1:]:
  if r == x:
    n += 1
  else:
    ans += n*(n-1)//2
    x = r
    n = 1
ans += n*(n-1)//2
print(ans)

