from collections import Counter

input()
A, B = map(int, input().split())
P = list(map(int, input().split()))

li = []
for i in P:
  if i <= A:
    li.append(1)
  elif A < i <= B:
    li.append(2)
  else:
    li.append(3)
    
cli = Counter(li)

if len(cli.keys()) != 3:
  print(0)
else:
  print(min(cli.values()))
