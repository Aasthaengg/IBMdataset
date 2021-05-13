N, M = map(int, input().split())
L = []
for i in range(N):
  L.append(list(map(int, input().split())))

S = [0]*M

for j in range (N):
  for k in range(1, L[j][0]+1):
    S[L[j][k]-1] += 1
    
print(S.count(N))