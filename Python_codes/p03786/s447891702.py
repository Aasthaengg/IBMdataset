N,*A = map(int, open(0).read().split())
A.sort(reverse=True)
s = sum(A)
ans = 1
for i in range(N):
  s -= A[i]
  if 2*s<A[i]:
    break
  ans += 1
print(ans)