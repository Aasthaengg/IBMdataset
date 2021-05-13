r, D, x = list(map(int, input().split()))
X = [x]
for i in range(11):
  X.append(r*X[i]-D)

for j in range(1,11):
  print(X[j])