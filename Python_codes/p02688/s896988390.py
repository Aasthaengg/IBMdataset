a, b = map(int, input().split())
oks = [0]*a
for i in range(b):
  d = int(input())
  snk = list(map(int, input().split()))
  for j in range(d):
    oks[snk[j]-1] += 1

print(oks.count(0))