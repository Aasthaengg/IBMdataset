N,u,v=map(int,input().split())

tree=[]
for i in range(N+1):
  tree.append([])

for i in range(N-1):
  A,B=map(int,input().split())
  tree[A].append(B)
  tree[B].append(A)
#print(u,v)
#print(tree)

dist_tak=[-1]*(N+1)
queue=[u]
d=0
while(len(queue)>0):
  new_queue=set()  
  for q in queue:
    if dist_tak[q]==-1:
      dist_tak[q]=d
      for q2 in tree[q]:
        new_queue.add(q2)
  d+=1
  queue=new_queue
#print(dist_tak)

dist_aok=[-1]*(N+1)
queue=[v]
d=0
while(len(queue)>0):
  new_queue=set()  
  for q in queue:
    if dist_aok[q]==-1:
      dist_aok[q]=d
      for q2 in tree[q]:
        new_queue.add(q2)
  d+=1
  queue=new_queue
#print(dist_aok)

answer=0
for i in range(1,N+1):
  if dist_tak[i]<dist_aok[i]:
    answer=max(answer,dist_aok[i]-1)
    
print(answer)