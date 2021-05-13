N = int(input())
A = list(map(int, input().split()))
D = {c:0 for c in range(N)}
for a in A:
  D[a-1] += 1
for d in D.values():
  print(d)