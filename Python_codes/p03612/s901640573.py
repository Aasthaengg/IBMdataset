n = int(input())
a = list(map(int, input().split()))
ans = 0
flg = 0
for i in range(n):
  if a[i] == i+1 and flg == 0:
    ans += 1
    flg = 1
  else:
    flg = 0
print(ans)