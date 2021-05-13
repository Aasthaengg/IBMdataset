N, K = map(int, input().split())
H = [int(i) for i in input().split()]
c = 0

for h in H:
  if h >= K:
    c += 1
print(c)