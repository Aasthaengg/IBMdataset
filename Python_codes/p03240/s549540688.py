n=int(input())
query=[]
for _ in range(n):
    a,b,c=map(int,input().split())
    query.append((a,b,c))
query=sorted(query, key=lambda x:x[2], reverse=True)

for cx in range(101):
  for cy in range(101):
      h=None
      flg=True
      for q in query:
        if h==None:
          h=q[2]+abs(cx-q[0])+abs(cy-q[1])
        elif q[2]!=0 and h!=q[2]+abs(cx-q[0])+abs(cy-q[1]):
          flg=False
          break
        elif q[2]==0 and h-abs(cx-q[0])-abs(cy-q[1])>0:
          flg=False
          break
      if flg: 
        print(cx,cy,h)
        exit()
