from collections import Counter
N = int(input())
*A, = map(int, input().split())
c = Counter(A)
for i in range(1, N+1):
  print(c[i])