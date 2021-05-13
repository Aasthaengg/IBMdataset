n = int(input())
info = []
mi = float('inf')
ma = 0
for _ in range(n):
  a,b = map(int, input().split())
  ma = max(ma, a)
  mi = min(mi,b)
print(ma+mi)