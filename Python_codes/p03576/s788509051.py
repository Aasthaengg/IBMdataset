N,K=map(int,input().split())

xlist,ylist,xylist=[],[],[]
xyset=set()
xydic={}
yxdic={}
for i in range(N):
  x,y=map(int,input().split())
  xlist.append(x)
  ylist.append(y)
  xylist.append((x,y))
  xyset.add((x,y))
  xydic[x]=y
  yxdic[y]=x

xy_prod_list=[]
for x in xlist:
  for y in ylist:
    xy_prod_list.append((x,y))
xy_prod_list.sort()
#print(xy_prod_list)    

num_ld_dic={}
for xx,yy in xy_prod_list:
  num_ld=0
  for x,y in xylist:
    if x<=xx and y<=yy:
      num_ld+=1
  num_ld_dic[(xx,yy)]=num_ld
#print(num_ld_dic)

answer=float("inf")
for i in range(len(xy_prod_list)):
  x1,y1=xy_prod_list[i]
  for j in range(len(xy_prod_list)):
    x2,y2=xy_prod_list[j]
    if x1>=x2 or y1>=y2:
      continue
    
    area=(x2-x1)*(y2-y1)
    if area>answer:
      continue
      
    num_point=num_ld_dic[(x2,y2)]-num_ld_dic[(x1,y2)]-num_ld_dic[(x2,y1)]+num_ld_dic[(x1,y1)]
    if (x1,y1) in xyset:  
      num_point+=1
    else:
      xx=yxdic[y1]
      if x1<=xx<=x2:
        num_point+=1
      yy=xydic[x1]
      if y1<=yy<=y2:
        num_point+=1
      
    if num_point>=K:
      #print((x1,y1),(x2,y2),num_point)
      answer=min(answer,area)
    
print(answer)