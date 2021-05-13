H,W=map(int,input().split())

mat=[[x=="#" for x in input()] for _ in range(H)]
#print(mat)

answer=0
visited_set=set()
for i in range(H):
  for j in range(W):
    if not mat[i][j] or (i,j) in visited_set:
      continue      

    queue=[(i,j)]
    d=0
    num_black=num_white=0
    while queue:
      new_queue=set()
      for q in queue:
        ii,jj=q
        visited_set.add((ii,jj))
        if d%2==0:
          num_black+=1
        else:
          num_white+=1
        
        if ii>0 and mat[ii][jj]!=mat[ii-1][jj] and not (ii-1,jj) in visited_set:
          new_queue.add((ii-1,jj))
        if ii<H-1 and mat[ii][jj]!=mat[ii+1][jj] and not (ii+1,jj) in visited_set:
          new_queue.add((ii+1,jj))
        if jj>0 and mat[ii][jj]!=mat[ii][jj-1] and not (ii,jj-1) in visited_set:
          new_queue.add((ii,jj-1))
        if jj<W-1 and mat[ii][jj]!=mat[ii][jj+1] and not (ii,jj+1) in visited_set:
          new_queue.add((ii,jj+1))
          
      queue=list(new_queue)
      d+=1
      
    #print(i,j,num_black,num_white)
    answer+=num_black*num_white

print(answer)