n,m,k = map(int, input().split( ))
A = list(map(int, input().split( )))
B = list(map(int, input().split( )))
acc1 = [0]
for i in range(n):
  acc1.append(acc1[-1] + A[i])
acc2 = [0]
for i in range(m):
  acc2.append(acc2[-1] + B[i])

ans = 0
j = m
for i in range(n+1):
  if acc1[i] > k:
    break
  while acc2[j] > k - acc1[i] and j > 0:
    j -= 1
  ans = max(ans,i+j)
print(ans)