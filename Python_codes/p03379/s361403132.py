import copy
N = int(input())
X = list(map(int, input().split()))
x = copy.copy(X)
x.sort()
left = x[N//2-1]
right = x[N//2]

for i in range(N):
  if X[i] <= left:
    print(right)
  else:
    print(left)