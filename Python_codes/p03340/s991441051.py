N, *A = map(int, open(0).read().split())
l = 0
r = 0
s = A[l]
x = A[l]
ans = 0
flag = True
for l in range(N):
  while s==x and flag:
    r += 1
    if r==N:
      flag = False
      break
    s += A[r]
    x ^= A[r]
  ans += r-l
  s -= A[l]
  x ^= A[l]
print(ans)