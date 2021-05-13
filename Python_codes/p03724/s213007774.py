import sys
n,m=map(int,input().split())
ctl=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  ctl[a-1]+=1
  ctl[b-1]+=1
for i in range(n):
  if ctl[i]%2==1:
    print('NO')
    sys.exit()
print('YES')