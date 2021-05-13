N=int(input())
d=[0]*N;D=[0]*N
s=0
for i in range(N):
  d[i],D[i]=map(int,input().split())
  if d[i]==D[i]:s+=1
  else:s=0
  if s==3:
    print('Yes')
    exit()
    
print('No')