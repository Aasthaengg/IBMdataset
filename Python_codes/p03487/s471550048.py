from collections import Counter
N = int(input())
a = list(map(int, input().split()))
c = Counter(a)
d = c.most_common()

ans = 0
for i in range(len(d)):
  num = d[i][0]
  cnt = d[i][1]
  if num > cnt:
    ans += cnt
  elif num < cnt:
    ans += cnt-num
print(ans)