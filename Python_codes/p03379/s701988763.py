N = int(input())
X = list(map(int, input().split()))

Y = sorted(X[:])
b_median = Y[N // 2 - 1]
a_median = Y[N // 2]

for i in range(N):
  if X[i] >= a_median:
    print(b_median)
  elif X[i] <= b_median:
    print(a_median)