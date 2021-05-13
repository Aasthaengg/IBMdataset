N, *A = map(int, open(0).read().split())
a = max(A,key=abs)
j = str(A.index(a)+1)
ans = []
if a>0:
  for i,c in enumerate(A):
    if c<0:
      ans.append(j+' '+str(i+1))
  for i in range(1,N):
    ans.append(str(i)+' '+str(i+1))
else:
  for i,c in enumerate(A):
    if c>0:
      ans.append(j+' '+str(i+1))
  for i in range(N,1,-1):
    ans.append(str(i)+' '+str(i-1))
print(len(ans))
print('\n'.join(ans))