n = int(input())
if n== 1:
  print(1)
  exit()
pos = []
diff = []
for _ in range(n):
  x,y = map(int,input().split())
  for px,py in pos:
    diff.append((x-px, y-py))
    diff.append((px-x, py-y))
  pos.append((x,y))
from collections import Counter
diff = Counter(diff).most_common()
x,y = diff[0][0]
count = diff[0][1]
if x== y == 0:
  x,y = diff[1][0]
  count = diff[1][1]
print(n-count)

