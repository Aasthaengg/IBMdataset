A = [int(x) for x in input().split()]
ans = 0
dic = {}
for x in A:
  if not x in dic:
    dic[x] = True
    ans += 1
print(ans)