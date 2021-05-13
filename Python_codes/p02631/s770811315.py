n = int(input())
A = list(map(int, input().split()))
x = 0
for a in A:
  x ^= a
L = []
for a in A:
  L.append(x^a)
print(*L)