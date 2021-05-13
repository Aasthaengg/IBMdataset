import copy
N=int(input())
X=list(map(int,input().split()))

Y=copy.copy(X)
Y.sort()
center = N//2
right = Y[center]
left = Y[center-1]
center_line = (right+left)/2

for i in range(N):
  if X[i] > center_line:
    print(left)
  else:
    print(right)