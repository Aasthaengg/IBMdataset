h,w,k=map(int,input().split())
ans=[[0]*w for i in range(h)]

num=0
for i in range(h):
 s=input()

 if '#' not in s:
  if i==0 or ans[i-1]==[0]*w:
   continue
  else:
   ans[i]=ans[i-1]

 else:
  for j in range(w):
   if s[j]=='#':
    num+=1
    ans[i][j]=num
   else:
    if j>=1 and ans[i][j-1]!=0:
     ans[i][j]=ans[i][j-1]

if ans[0]==[0]*w:
 i=0
 while ans[i]==[0]*w:
  i+=1
 for j in range(i):
  ans[j]=ans[i]

for i in range(h):
 if ans[i][0]==0:
  j=0
  while ans[i][j]==0:
   j+=1
  for k in range(j):
   ans[i][k]=ans[i][j]

for i in range(h):
 print(*ans[i])