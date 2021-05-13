def find():
    h,w,m=map(int,input().split())
    idx=[]


    for i in range(m):
      var=list(map(int,input().split()))
      idx.append(var)


    r={}
    c={}
    #maze=[[0 for j in range(w)]for i in range(h)]
    mz={}

    for i in idx:
      mz.setdefault((i[0]-1,i[1]-1),0)
      mz[(i[0]-1,i[1]-1)]=1
      #maze[i[0]-1][i[1]-1]=1
      r.setdefault(i[0]-1,0)
      r[i[0]-1]+=1
      c.setdefault(i[1]-1,0)
      c[i[1]-1]+=1

    ans=0
    maxval=0



    row=[]
    col=[]
    maxr=max(r.values())
    maxc=max(c.values())
    for i in range(h):
      r.setdefault(i,0)
      if r[i]==maxr:
        row.append(i)
      

    for j in range(w):
      c.setdefault(j,0)
      if c[j]==maxc:
        col.append(j)
    
    for i in row:
      for j in col:
        mz.setdefault((i,j),0)
        if(mz[(i,j)]==0):
          return maxc+maxr
         
    return maxc+maxr-1
 
print(find())