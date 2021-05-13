n,k=map(int,input().split())
if k>(n-1)*(n-2)//2:print(-1);exit()
e=[]
for i in range(1,n):e.append((0,i))
ee=[]
for i in range(1,n-1):
  for j in range(i+1,n):
    ee.append((i,j))
for i in range((n-1)*(n-2)//2-k):
  e.append(ee[i])
print(len(e))
for i,j in e:print(i+1,j+1)