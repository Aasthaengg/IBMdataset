n = int(input())

A = list(map(int, input().split()))

s = sum(A)

L = [0 for i in range(10**5 + 1)]

for i in range(n):
  L[A[i]] += 1

q = int(input())

for i in range(q):
  b, c = map(int, input().split())
  s += (c - b) * L[b]
  print(s)
  tmp = L[b]
  L[b], L[c] = 0, tmp + L[c]