N = int(input())
L = [2,1]
for i in range(N):
  x = L[i+1] + L[i]
  L.append(x)
print(L[N])