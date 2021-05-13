N = int(input())
a = {i + 1: int(input()) for i in range(N)}
ans = -1

count = 1
nxt = 1
while count < N:
  nxt = a[nxt]
  if nxt == 2:
    ans = count
    break
  count += 1

print(ans)
