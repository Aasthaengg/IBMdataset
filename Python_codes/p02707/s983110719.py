import collections
N = int(input())
A = list(map(int, input().split()))
count = collections.Counter(A)
for n in range(N):
  print(count[n+1])