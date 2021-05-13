N = int(input())
L = list(map(int, input().split()))
 
ans = 0
if(N >= 3):
  t = []
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if((L[i] != L[j]) & (L[i] != L[k]) & (L[j] != L[k]) & (abs(L[j]-L[k]) < L[i]) & (L[i] < L[j]+L[k])): t.append((L[i], L[j], L[k]))
  ans = len(t)

print(ans)