N = int(input())
H = list(map(int, input().split()))
L = [0]*N
L[1] = abs(H[1] - H[0])
for i in range (2,N):
  X = L[i-1] + abs(H[i] - H[i-1])
  Y = L[i-2] + abs(H[i] - H[i-2])
  L[i] = min(X,Y)
print(L[N-1])