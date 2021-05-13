N = int(input())
L = list(map(int, input().split()))
L.sort()

count = 0
for k in range(2, N):
  for j in range(1,k):
    for i in range(j):
      if L[i] + L[j] > L[k] and L[i] != L[j] and L[j] != L[k]:
        count += 1
      else:
        continue
        
print(count)