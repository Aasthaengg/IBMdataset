from collections import Counter

h, w = map(int, input().split())
A = []
for _ in range(h):
  A += list(input())
C = Counter(A)
X = [0]*2
for i in C.values():
  if i%2:
    X[0] += 1
  if i%4>=2:
    X[1] += 1
if X[0] <= (h%2)*(w%2) and X[1] <= (h%2) * (w//2) + (w%2) * (h//2):
  print("Yes")
else:
  print("No")