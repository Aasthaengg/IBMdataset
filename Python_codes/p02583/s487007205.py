N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if A[i] != A[j] and A[j] != A[k] and A[k] != A[i] and (A[i] + A[j]>A[k]) and (A[j] + A[k]>A[i]) and (A[k] + A[i]>A[j]):
        count = count + 1

print(count)

