A, B, K = (int(x) for x in input().split())
p = []
i = 0
m = min(A,B)
for i in range(1,m+1):
  if A%i == 0 and B%i == 0:
    p.append(i)
p.sort()
print(p[len(p)-K])