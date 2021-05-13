from collections import Counter
from sys import exit
N = int(input())
D = Counter(map(int, input().split()))
M = int(input())
T = tuple(map(int, input().split()))
for t in T:
  if D.get(t):
    D[t] -= 1
  else:
    print("NO")
    exit()
print("YES")