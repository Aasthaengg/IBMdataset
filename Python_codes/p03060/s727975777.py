N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
v = 0

for i in range(N):
  if X[i] - Y[i] > 0:
    v += X[i]-Y[i]
    
print(v)