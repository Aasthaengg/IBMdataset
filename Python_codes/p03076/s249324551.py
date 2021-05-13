L = []
R = []

for _ in range(5):
  x = int(input())
  L.append(x)
  R.append(-x%10)

print(sum(L)+sum(R)-max(R))