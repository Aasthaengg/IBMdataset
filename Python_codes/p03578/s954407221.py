from collections import Counter
N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

CD = Counter(D)
CT = Counter(T)
ans = CT - CD

if ans:
  print('NO')
else:
  print('YES')