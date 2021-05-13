from collections import Counter
n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
ans = [0]*2
t = 0
for i in sorted(count.items(), reverse=True):
  if i[1] >= 4:
    if t == 0:
      ans[0],ans[1] = i[0],i[0]
      t = 2
    elif t == 1:
      ans[t] = i[0]
      t += 1
  elif i[1] >= 2:
    ans[t] = i[0]
    t += 1
  if t == 2: break
print(ans[0]*ans[1])