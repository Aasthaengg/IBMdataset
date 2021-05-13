import sys
n,m=map(int,input().split())
sc=[list(map(int,input().split())) for i in range(m)]

num=['_']*n

if n==1 and m==0:
    print('0')
    sys.exit()

if n==1 and m==1 and sc[0][1]==0:
    print('0')
    sys.exit()

for i in range(m):
  if num[sc[i][0]-1]!='_' and num[sc[i][0]-1]!=sc[i][1]:
    print('-1')
    sys.exit()
  else:
    num[sc[i][0]-1]=sc[i][1]

if num[0]==0:
  print('-1')
  sys.exit()
    
if num[0]=='_':
    num[0]=1
    
for i in range(1,n):
    if num[i]=='_':
      num[i]=0
      
print(''.join(map(str,num)))