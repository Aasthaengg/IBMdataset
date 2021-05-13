n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
if n<m:
  print('NO')
  exit()
d.sort()
t.sort()
i=0
j=0
while i<n and j<m:
  if d[i]==t[j]:
    i+=1
    j+=1
  else:
    i+=1
if j==m:
  print('YES')
else:
  print('NO')