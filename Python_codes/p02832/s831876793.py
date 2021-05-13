N = int(input())
A = list(map(int, input().split()))

k = 1
ans = 0

if 1 not in A:
  print(-1)
  exit()

for a in A:
  if a == k:
    k += 1
  else:
    ans += 1

print(ans)