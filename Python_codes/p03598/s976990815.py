N = int(input())
K = int(input())
xs = list(map(int,input().split()))

d = 0
for x in xs:
  kd = min(x,K-x)
  d += 2*kd
print(d)