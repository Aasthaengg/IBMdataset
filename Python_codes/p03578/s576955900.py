from collections import Counter
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

c = Counter(D)
flag = True
for t in T:
  if c[t] > 0:
    c[t] -= 1
  else:
    flag = False
    break
    
if flag:
  print('YES')
else:
  print('NO')