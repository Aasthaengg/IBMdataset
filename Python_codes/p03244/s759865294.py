from collections import Counter
from heapq import heappop,heappush

N = int(input())
V = list(map(int, input().split()))
odd = Counter(V[::2])
odd[10**6] = 0
even = Counter(V[1::2])
even[10**6] = 0
heapodd = []
heapeven = []
for k,v in odd.items():
    heappush(heapodd,(-v,k))
for k,v in even.items():
    heappush(heapeven,(-v,k))

vo1,odd1 = heappop(heapodd)
vo2,odd2 = heappop(heapodd)
ve1,even1 = heappop(heapeven)
ve2,even2 = heappop(heapeven)

if odd1 != even1:
  print(N + vo1 + ve1)
else:
  print(min(N+ve1+vo2,N+vo1+ve2))