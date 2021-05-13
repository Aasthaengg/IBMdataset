from heapq import heappop, heapify

s = input()
N = len(s)
K = int(input())

sub = set()
for i in range(N):
  for j in range(5):
    if i+j+1 <= N:
      sub.add(s[i:i+j+1])

sub = list(sub)
heapify(sub)
for i in range(K-1):
  _ = heappop(sub)
print(heappop(sub))
