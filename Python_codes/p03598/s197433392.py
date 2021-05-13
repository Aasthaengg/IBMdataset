N = int(input())
K = int(input())
X = input().split(' ')
X = [int(X[i]) for i in range(len(X)) ]
distance = 0
for i in range(N):
  if abs(X[i]) - abs(X[i]-K) > 0:
    distance += abs(X[i]-K)*2
  else:
    distance += abs(X[i])*2
print(distance)