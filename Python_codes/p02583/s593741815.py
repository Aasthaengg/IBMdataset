N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
cnt = 0

for i in range(N-2):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if L[i] != L[j] != L[k] and L[i] + L[j] > L[k]:
        cnt += 1
        
print(cnt)