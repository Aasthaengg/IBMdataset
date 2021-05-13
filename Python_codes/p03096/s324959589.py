N = int(input())
MODN = int(1e9 + 7)

D = {}
X = [0] * N

for i in range(N):
  c = int(input())
  if not c in D:
    X[i] = 1 if i == 0 else X[i-1]
    D[c] = i
    continue
    
  X[i] = (X[i-1] + X[D[c]]) % MODN if D[c] < i-1 else X[i-1]
  D[c] = i
    
print(X[N-1])