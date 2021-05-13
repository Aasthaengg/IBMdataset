n, x = map(int, input().split())
L = list(map(int, input().split()))

ans = 1
D_i = 0
for l in L:
  D_i += l
  if D_i <= x:
    ans += 1

print(ans)
