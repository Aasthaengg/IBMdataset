n, x = map(int, input().split())
Ls = list(map(int, input().split()))
ans = 1
temp = 0
for l in Ls:
  temp += l
  if temp <= x:
    ans += 1
print(ans)