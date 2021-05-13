n,m=map(int,input().split())

x=[input() for i in range(n)]
y=[input() for i in range(m)]

ans='No'

for i in range(n-m+1):
  for j in range(n-m+1):
    maze=[]
    for k in range(m):
      pin=''
      for l in range(m):
        pin+=x[i+k][j+l]
      
      maze.append(pin)

    if maze==y:
      ans='Yes'
      break


print(ans)