from collections import defaultdict
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

p = defaultdict(int)
for d in D:
  p[d] += 1

for t in T:
  if p[t] == 0:
    print("NO")
    exit(0)
  else:
    p[t] -= 1

print("YES")
