n=int(input())
m=n-n%2+1
d=[[i+j+2!=m and i!=j for i in range(n)] for j in range(n)]
print(sum([sum(i) for i in d])//2)
for i in range(n):
  for j in range(i+1,n):
    if d[i][j]:print(i+1,j+1)