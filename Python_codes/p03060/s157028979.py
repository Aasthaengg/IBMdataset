N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

toku = 0
total = 0

for i in range(N):
  toku = V[i] - C[i]
  if toku > 0:
    total += toku
print(total)