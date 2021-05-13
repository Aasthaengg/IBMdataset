N, M = map(int, input().split())
Lmi, Lma = [], []
for i in range(M):
  mi, ma = map(int, input().split())
  Lmi.append(mi)
  Lma.append(ma)
r = max(min(Lma) - max(Lmi) + 1, 0)
print(r)
