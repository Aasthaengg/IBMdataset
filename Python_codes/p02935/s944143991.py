N = int(input())
V = list(map(lambda v: int(v), input().split(" ")))
V.sort()

a = V[0]
for i in range(len(V) - 1):
  a = (a + V[i + 1])/2

print(a)