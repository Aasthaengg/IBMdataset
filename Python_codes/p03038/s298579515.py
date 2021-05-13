N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = []
for i in range(M):
  tmp = list(map(int, input().split()))
  BC.append(tmp)

A.sort()
BC.sort(key=lambda x: x[1], reverse=True)

j = 0
for i in range(M):
  count = 0
  while A[j] < BC[i][1]:
    A[j] = BC[i][1]			# 値を置き換える
    j += 1
    count += 1
    if count == BC[i][0] or j == N:
      break
  if j == N:
    break
print(sum(A))