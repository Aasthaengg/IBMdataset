n = int(input())
plst = list(map(int, input().split()))
flg = False
ans = 0
for i, p in enumerate(plst, start = 1):
  if flg:
    flg = False
    continue
  if i == p:
    flg = True
    ans += 1
print(ans)
