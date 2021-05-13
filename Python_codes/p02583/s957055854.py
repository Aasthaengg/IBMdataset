n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum_ = sum([l[i], l[j], l[k]])
      max_ = max([l[i], l[j], l[k]])
      if l[i] != l[j] and l[i] != l[k] and l[j] != l[k] and (sum_ - max_) > max_:
        cnt += 1
print(cnt)