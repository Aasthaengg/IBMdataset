N = int(input())
K = int(input())
X = [int(i) for i in input().split()]

d = 0

for x in X:
  d += 2*min(abs(K-x),x)

print(d)