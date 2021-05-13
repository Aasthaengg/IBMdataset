n=int(input())
t=[0]*(n+1)
x=[0]*(n+1)
y=[0]*(n+1)
for i in range(n):
  t[i+1],x[i+1],y[i+1]=map(int,input().split())
  
  lim_t=t[i+1]-t[i]
  lim_x=x[i+1]-x[i]
  lim_y=y[i+1]-y[i]
  
  if abs(lim_x)+abs(lim_y)>lim_t or (lim_t-lim_x-lim_y)%2==1:
    print('No')
    exit()
    
print('Yes')