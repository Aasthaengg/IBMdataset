X,Y,N=map(int,input().split())
max_X=X
max_Y=Y
current_min_x=0
current_min_y=0
current_max_x=X
current_max_y=Y
xy=[list(map(int,input().split())) for _ in range(N)]
for x,y,a in xy:
  n=0
  if a==1:
    current_min_x=max(current_min_x, x)
  elif a==2:
    current_max_x=min(current_max_x, x)
  elif a==3:
    current_min_y=max(current_min_y, y)
  elif a==4:
    current_max_y=min(current_max_y, y)
result=(current_max_x-current_min_x)*(current_max_y-current_min_y)
print(max(current_max_x-current_min_x,0)*max(current_max_y-current_min_y,0))