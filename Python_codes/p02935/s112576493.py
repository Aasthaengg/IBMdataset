N = int(input())
v = list(map(int, input().split()))
V = sorted(v, reverse=True)
A = 0

while N > 1:
  v1 = V.pop()
  v2 = V.pop()
  A = (v1 + v2)/2
  V.append(A)
  N -= 1

print(V[0])