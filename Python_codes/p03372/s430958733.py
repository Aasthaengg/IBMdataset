N,C = map(int,input().split())
L = []
for i in range(N):
  L.append(list(map(int,input().split())))
A = [0]
B = [0]
k = 0
for i in range(N):
  k += L[i][1]
  p = max(A[i],k-L[i][0])
  A.append(p)
k = 0
for i in range(N):
  k += L[N-i-1][1]
  p = max(B[i],k-(C-L[N-i-1][0]))
  B.append(p)
ans = max(A[N],B[N])
t = 0
for i in range(N):
  b = L[N-i-1][0]
  t += L[N-i-1][1]
  if ans <= t-2*(C-b)+A[N-i-1]:
    ans = t-2*(C-b)+A[N-i-1]
t = 0
for i in range(N):
  a = L[i][0]
  t += L[i][1]
  if ans <= t-2*a+B[N-i-1]:
    ans = t-2*a+B[N-i-1]
print(ans)