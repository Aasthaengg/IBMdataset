N = int(input())
X = list(map(int, input().split()))
S = [0]*100
for i in range(1,101):
  sum = 0
  for j in range(N):
    sum += (X[j]-i)**2
  S[i-1] = sum
print(min(S))
