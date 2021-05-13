H,W=map(int,input().split())

queue=[]
mat=[[True]*(W+2)]
for i in range(1,H+1):
  array=[True]+[x=="#" for x in input()]+[True]
  mat.append(array)
  for j in range(1,W+1):
    if array[j]:
      queue.append((i,j))
mat.append([True]*(W+2))
#print(mat)
#print(queue)

d=0
while queue:
  new_queue=set()
  for q in queue:
    i,j=q
    #print(q)
    if not mat[i-1][j]:
      new_queue.add((i-1,j))
      mat[i-1][j]=True
    if not mat[i+1][j]:
      new_queue.add((i+1,j))
      mat[i+1][j]=True
    if not mat[i][j-1]:
      new_queue.add((i,j-1))
      mat[i][j-1]=True
    if not mat[i][j+1]:
      new_queue.add((i,j+1))
      mat[i][j+1]=True
      
  queue=list(new_queue)
  d+=1
  
print(d-1)