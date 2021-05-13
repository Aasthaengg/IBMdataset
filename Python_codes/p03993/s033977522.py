N,*A = map(int,open(0).read().split())
cnt=0
for i,a in enumerate(A):
  if i+1 == A[a-1]:
    cnt+=1
print(cnt//2)