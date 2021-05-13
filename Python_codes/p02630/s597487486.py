N = int(input())
A = [int(x) for x in input().split()]
S =sum(A)
D = [0]*(10**5+1)
for a in A:
  D[a] += 1
Q = int(input())
for i in range(Q):
  b, c = map(int, input().split())
  S -= D[b]*b
  S += D[b]*c
  D[c] += D[b]
  D[b] = 0
  print(S)