N = int(input())
A = list(map(int, input().split()))

cnt = 0
l = []
for a in A:
  if a < 0:
    cnt += 1
  l.append(abs(a))

if cnt % 2 == 0:
  ans = sum(l)
else:
  ans = sum(l) - 2*min(l)
print(ans)