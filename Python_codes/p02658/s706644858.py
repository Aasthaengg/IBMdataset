n = int(input())
aa = list(map(int, input().split()))
if 0 in aa:
  print(0)
  exit()
ans = 1
for a in aa:
  ans *= a
  if ans > 10 ** 18:
    print(-1)
    exit()
print(ans)