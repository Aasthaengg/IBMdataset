N,D=map(int,input().split(' '))
#X=[]
#Y=[]
D2=D**2
ans=0

for i in range(N):
  x,y=map(int,input().split(' '))
  if x**2+y**2<=D2:
    ans+=1
  #X.append(x)
  #Y.append(y)



print(ans)