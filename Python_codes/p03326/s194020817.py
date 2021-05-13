import sys
N,M=map(int,input().split())

if M==0:
  print(0)
  sys.exit(0)

xyzlist=[]
for i in range(N):
  x,y,z=map(int,input().split())
  xyzlist.append((x,y,z))
#print(xyzlist)

selected_list1=[False]*N
pt_list=[0,0,0]
for _ in range(M):
  max_ind=-1
  max_point=-10**20
  for i in range(N):
    if selected_list1[i]:
      continue
      
    x,y,z=xyzlist[i]    
    point=abs(pt_list[0]+x)-abs(pt_list[0])+abs(pt_list[1]+y)-abs(pt_list[1])+abs(pt_list[2]+z)-abs(pt_list[2])
    if max_point<point:
      max_ind=i
      max_point=point
      
  #print(max_ind+1,xyzlist[max_ind])  
  selected_list1[max_ind]=True
  mx,my,mz=xyzlist[max_ind]
  pt_list=[pt_list[0]+mx,pt_list[1]+my,pt_list[2]+mz]
  #print(pt_list)
  
#print(selected_list1)
#print(pt_list)
answer1=0
for i in range(3):
  answer1+=abs(pt_list[i])
#print(answer1)

maxabs_ind=[-1,-1,-1]
maxabs=[-1,-1,-1]
for i in range(N):
  x,y,z=xyzlist[i]
  if abs(x)>maxabs[0]:
    maxabs_ind[0]=i
    maxabs[0]=abs(x)
  if abs(y)>maxabs[1]:
    maxabs_ind[1]=i
    maxabs[1]=abs(y)
  if abs(z)>maxabs[2]:
    maxabs_ind[2]=i
    maxabs[2]=abs(z)
#print(maxabs_ind)
    
selected_list2=[False]*N
selected_list2[maxabs_ind[0]]=True
pt_list=list(xyzlist[maxabs_ind[0]])
#print(pt_list)
for _ in range(M-1):
  max_ind=-1
  max_point=-10**20
  for i in range(N):
    if selected_list2[i]:
      continue
      
    x,y,z=xyzlist[i]    
    point=abs(pt_list[0]+x)-abs(pt_list[0])+abs(pt_list[1]+y)-abs(pt_list[1])+abs(pt_list[2]+z)-abs(pt_list[2])
    if max_point<point:
      max_ind=i
      max_point=point
      
  #print(max_ind+1,xyzlist[max_ind])  
  selected_list2[max_ind]=True
  mx,my,mz=xyzlist[max_ind]
  pt_list=[pt_list[0]+mx,pt_list[1]+my,pt_list[2]+mz]
  #print(pt_list)
  
#print(selected_list2)
#print(pt_list)
answer2=0
for i in range(3):
  answer2+=abs(pt_list[i])
#print(answer2)

selected_list3=[False]*N
selected_list3[maxabs_ind[1]]=True
pt_list=list(xyzlist[maxabs_ind[1]])
#print(pt_list)
for _ in range(M-1):
  max_ind=-1
  max_point=-10**20
  for i in range(N):
    if selected_list3[i]:
      continue
      
    x,y,z=xyzlist[i]    
    point=abs(pt_list[0]+x)-abs(pt_list[0])+abs(pt_list[1]+y)-abs(pt_list[1])+abs(pt_list[2]+z)-abs(pt_list[2])
    if max_point<point:
      max_ind=i
      max_point=point
      
  #print(max_ind+1,xyzlist[max_ind])  
  selected_list3[max_ind]=True
  mx,my,mz=xyzlist[max_ind]
  pt_list=[pt_list[0]+mx,pt_list[1]+my,pt_list[2]+mz]
  #print(pt_list)
  
#print(selected_list3)
#print(pt_list)
answer3=0
for i in range(3):
  answer3+=abs(pt_list[i])
#print(answer3)

selected_list4=[False]*N
selected_list4[maxabs_ind[2]]=True
pt_list=list(xyzlist[maxabs_ind[2]])
#print(pt_list)
for _ in range(M-1):
  max_ind=-1
  max_point=-10**20
  for i in range(N):
    if selected_list4[i]:
      continue
      
    x,y,z=xyzlist[i]    
    point=abs(pt_list[0]+x)-abs(pt_list[0])+abs(pt_list[1]+y)-abs(pt_list[1])+abs(pt_list[2]+z)-abs(pt_list[2])
    if max_point<point:
      max_ind=i
      max_point=point
      
  #print(max_ind+1,xyzlist[max_ind])  
  selected_list4[max_ind]=True
  mx,my,mz=xyzlist[max_ind]
  pt_list=[pt_list[0]+mx,pt_list[1]+my,pt_list[2]+mz]
  #print(pt_list)
  
#print(selected_list3)
#print(pt_list)
answer4=0
for i in range(3):
  answer4+=abs(pt_list[i])
#print(answer4)

#print(answer1,answer2,answer3,answer4)
print(max(answer1,answer2,answer3,answer4))
