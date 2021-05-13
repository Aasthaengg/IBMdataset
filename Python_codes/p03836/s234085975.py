x1,y1,x2,y2=map(int,input().split())
ans=[]
for i in range(y2-y1):
  ans.append('U')
for i in range(x2-x1):
  ans.append('R')
for i in range(y2-y1):
  ans.append('D')
for i in range(x2-x1):
  ans.append('L')
ans.append('L')
for i in range(y2-y1+1):
  ans.append('U')
for i in range(x2-x1+1):
  ans.append('R')
ans.append('D')
ans.append('R')
for i in range(y2-y1+1):
  ans.append('D')
for i in range(x2-x1+1):
  ans.append('L')
ans.append('U')
print(''.join(ans))