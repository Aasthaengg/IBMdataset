from collections import Counter
n = int(input())
a = list(map(int, input().split()))
d = Counter(a)
k = d.most_common(1)[0][1]
if k>=2:
  print('NO')
else:
  print('YES')