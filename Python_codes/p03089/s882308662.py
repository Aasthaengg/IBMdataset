N,*B = map(int, open(0).read().split())
ans = [0]*N
for i in range(N):
  for j in range(len(B)-1,-1,-1):
    if B[j]==j+1:
      ans[N-1-i] = j+1
      B = B[:j]+B[j+1:]
      break
if B==[]:
  print('\n'.join(map(str,ans)))
else:
  print(-1)