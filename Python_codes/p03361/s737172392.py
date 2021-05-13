import sys
h,w=map(int,input().split())
a=[]
for i in range(h):
  a.append(input())
for i in range(h):
  for j in range(w):
    if a[i][j]=='#':
      flag=1
      if i>0 and a[i-1][j]=='#':
        flag=0
      if j>0 and a[i][j-1]=='#':
        flag=0
      if i<h-1 and a[i+1][j]=='#':
        flag=0
      if j<w-1 and a[i][j+1]=='#':
        flag=0
      if flag==1:
        print('No')
        sys.exit()
print('Yes')