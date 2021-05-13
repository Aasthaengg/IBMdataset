N=int(input())
L=list(map(int, input().split()))

L=sorted(L)
c=0
for i in range(N-1):
  c+=L[i]
if L[N-1]<c:
  print('Yes')
else:print('No')