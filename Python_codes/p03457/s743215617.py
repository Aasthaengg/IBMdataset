N=int(input())+1
t,x,y,r=[0]*N,[0]*N,[0]*N,1
N-=1
for i in range(N):
    i+=1
    t[i],x[i],y[i]=map(int,input().split())

def a(t,x,y):
    return (x+y<=t)*(1-(x+y-t)%2)

for i in range(N):
    r*=a(t[i+1]-t[i],abs(x[i+1]-x[i]),abs(y[i+1]-y[i]))
print(['No','Yes'][r])