n=int(input())
ans = {}
printed = 0
for i in range(n):
  a = int(input())
  if not a in ans:
    ans[a] = 1
    printed += 1
  else:
    ans[a] += 1
    if ans[a] % 2 == 0:
      printed -= 1
    else:
      printed += 1
print(printed)