x,y=map(int,input().split())
x0=x
y0=y
X=[1,1,-1,-1]
Y=[1,-1,1,-1]
l=[]
for i in range(4):
    x=x*X[i]
    y=y*Y[i]
    q=10**10
    if y-x>=0:
      q=y-x
      if X[i]==-1:
        q+=1
      if Y[i]==-1:
        q+=1
    l.append(q)
    x=x0
    y=y0
    
print(min(l))