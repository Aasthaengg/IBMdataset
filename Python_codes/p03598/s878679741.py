N = int(input())
K = int(input())
xs = list(map(int, input().split()))

dist = 0

for x in xs:
  dist += min(x, K-x)
  
print(dist*2)