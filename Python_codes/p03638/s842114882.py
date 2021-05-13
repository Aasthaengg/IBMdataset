h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
m=[[0]*(w+2) for _ in range(h+2)]
#print(m)
x=y=1
for i in range(n):
  cnt=a[i]
  #print(i+1)
  while cnt>0:
    #print(x,y)
    m[x][y]=i+1
    cnt-=1
    if y+1<=w and m[x][y+1]==0:
        y+=1
    elif y-1>0 and  m[x][y-1]==0:
        y-=1
    else:
      x+=1
  #print(m,end=" after cnti\n")
for i in range(h):
  for j in range(w):
    print(m[i+1][j+1],end=' ') if j!=w-1 else print(m[i+1][j+1])
  #print('\n')
      
