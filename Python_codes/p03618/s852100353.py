A = input()
N = len(A)
count = {}
ans = 1

for i in range(N):
  if A[i] in count.keys():
    count[A[i]] += 1
  else:
    count[A[i]] = 1

L = list(count.values())
M = len(L)
for i in range(M):
  for j in range(i+1,M):
    ans += L[i] * L[j]
    
print(ans)