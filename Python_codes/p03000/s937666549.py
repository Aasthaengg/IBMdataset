n, x = map(int, input().split())
Ls = list(map(int, input().split()))
ans = 1
target = 0
for l in Ls:
  target += l
  if target <= x:
    ans += 1
  else:
    print(ans)
    exit()
print(ans)