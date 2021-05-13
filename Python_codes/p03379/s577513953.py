N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)
m1 = Y[N//2-1]
m2 = Y[N//2]

for x in X:
  if x<m2:
    print(m2)
  else:
    print(m1)