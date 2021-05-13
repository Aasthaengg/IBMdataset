n = int(input())
blst = list(map(int, input().split()))
if 1 not in blst:
  print(-1)
  exit()
cnt = 0
for i in range(n):
  if cnt + 1 == blst[i]:
    cnt += 1
print(n - cnt)

