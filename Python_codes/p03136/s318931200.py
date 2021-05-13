N=int(input())
L=list(map(int,input().split()))
a=sum(L)
flag=True
for i in range(N):
  if a<=2*L[i]:
    flag=False
    break
if flag:
  print('Yes')
else:
  print('No')