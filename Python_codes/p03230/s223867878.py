n=int(input())
if n==1:
  print('Yes')
  print('2\n1 1\n1 1')
  exit()
for i in range(n):
  if i*(i+1)//2==n:break
else:
  print('No')
  exit()
m=i
a=[[0]*m for _ in range(m)]
i=0
while n>0:
  for j in range(i+1):
    a[i][j]=n
    n-=1
  i+=1
a=a[::-1]
s=[[] for _ in range(m+1)]
for i in range(m):
  s[i]=a[i][:m-i]
  for j in range(i):
    s[i]+=[a[i-1-j][m-i-1]]
for i in range(m):
  s[-1]+=[a[i][m-i-1]]
print('Yes')
print(len(s))
for i in s:
  print(len(i),*i)