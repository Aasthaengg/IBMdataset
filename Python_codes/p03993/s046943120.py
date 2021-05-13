n = int(input())
a = list(map(int, input().split()))

d = {}
ans = 0
for num,i in enumerate(a,1):
  if i not in d: d[num] = i
  else:
    if d[i] == num: ans += 1
print(ans)