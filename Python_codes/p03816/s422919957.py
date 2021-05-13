N, *A = map(int, open(0).read().split())
cnt = 0
log = [0]*(max(A)+1)
for i in range(N):
  c = A[i]
  if log[c]!=0:
    cnt += 1
  else:
    log[c] = 1
if cnt%2==0:
  print(N-cnt)
else:
  print(N-cnt-1)