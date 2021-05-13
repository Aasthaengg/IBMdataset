from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
D = defaultdict(int)

for i in A:
  D[i] += 1

for i in range(N):
  print(D[i+1])