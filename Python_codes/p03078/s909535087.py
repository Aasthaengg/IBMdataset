import sys
readline = sys.stdin.readline

X,Y,Z,K = map(int,readline().split())

A = sorted(list(map(int,readline().split())),reverse = True)
B = sorted(list(map(int,readline().split())),reverse = True)
C = sorted(list(map(int,readline().split())),reverse = True)

# AとBを組み合わせたケーキの上位K位を作る
AB = []
for a in range(len(A)):
  for b in range(len(B)):
    AB += [A[a] + B[b]]
    
AB = sorted(AB,reverse = True)[:K]

# ABとCを組み合わせたケーキの上位K位を作る
ans = []
for ab in range(len(AB)):
  for c in range(len(C)):
    ans += [AB[ab] + C[c]]
    
ans = sorted(ans,reverse = True)[:K]
for a in ans:
  print(a)