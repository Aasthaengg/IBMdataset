s = input()
K = int(input())

ans = []

for index, i in enumerate(s):
  ans.append(i)

  count = 1
  now = i
  for indexs, k in enumerate(s):
    if indexs <= index:
      continue
      
    if count >= 5:
      break

    now += k
    ans.append(now)
    count += 1

ans = list(set(ans))
ans.sort()
print(ans[K-1])