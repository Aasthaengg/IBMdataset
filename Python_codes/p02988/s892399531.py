n = int(input())
p = list(map(int, input().split()))
c = 0
for i in range(2,n):
  p1 = p[i-2]
  p2 = p[i-1]
  p3 = p[i]
  if p1 < p2 < p3 or p3 < p2 < p1:
    c += 1
print(c)