N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

diff = [0]
for n in range(N):
  if V[n] - C[n] > 0:
    diff.append(V[n] - C[n])

print(sum(diff))