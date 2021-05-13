from collections import Counter

N, M = map(int, input().split())
li = []
for _ in range(M):
  a, b = map(int, input().split())
  li.append(a)
  li.append(b)
  
cli = Counter(li)
if all([v % 2 == 0 for i, v in cli.items()]):
  print("YES")
else:
  print("NO")