n=int(input())
h=list(map(int,input().split()))
m=h[0]
for i in range(1,n):
  if m-h[i]>1:
    print('No')
    break
  m=max(m,h[i])
else:print('Yes')