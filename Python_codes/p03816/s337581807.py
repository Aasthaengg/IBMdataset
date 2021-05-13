from collections import defaultdict
d = defaultdict(int)

N = int(input())
A = list(map(int, input().split()))

x = 0
y = 0

for a in A:
  d[a] += 1
  
for i in d:
  if d[i] >= 2:
    x += 1
    y += d[i] - 1
    
if y % 2 == 0:
  print(N-y)
else:
  print(N-y-1)