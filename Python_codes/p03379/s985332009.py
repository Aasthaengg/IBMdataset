from statistics import *
N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)
m = median(X)

for x in X:
  if x<=m:
    print(Y[N//2])
  else:
    print(Y[N//2-1])