n,m = map(int,input().split())
a=[]
for _ in range(n):
  a.append(list(map(int,input().split())))

x = [0]*m

for i in range(n):
  for k in range(1,a[i][0]+1):
    x[a[i][k]-1] += 1
count = 0
for i in range(m):
  if x[i] == n:
    count += 1
print(count)