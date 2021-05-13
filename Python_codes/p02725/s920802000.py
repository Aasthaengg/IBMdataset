K, N = map(int, input().split())
A = list(map(int, input().split()))
length = []

for i in range(N-1):
  length.append(abs(A[i]-A[i+1]))


length.append(K-sum(length))

max_l = length[0]
for j in range(N):
  if max_l <= length[j]:
    max_l = length[j]
  else:
    pass


length.remove(max_l)
result = sum(length)
print(result)