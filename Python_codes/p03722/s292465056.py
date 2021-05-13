#nに行くまでの道で正の閉路があればいくらでも大きくすることができる
n,m=list(map(int,input().split()))
es=[]
for i in range(m):
  a,b,c=map(int,input().split())
  es.append((a-1,b-1,c))

def BellmanFord(n,s,es):
  d=[-float("INF")]*n
  d[s]=0
  cnt=0
  while(1):
    update=False
    for p,q,r in es:
      if d[p]!=-float("INF") and d[q]<d[p]+r:
        d[q]=d[p]+r
        update=True
    cnt+=1
    if not update:
      break
    if cnt==n:
      #負の経路がある場合
      #さらにこっからn回繰り返してd[n-1]が更新されるかみる
      negative=[False]*n
      for i in range(n):
        for p,q,r in es:
          if d[q]<d[p]+r:
            negative[q]=True
            d[q]=d[p]+r
      if negative[n-1]==True:
        print("inf")
        exit()
      else:
        print(d[n-1])
        exit()
        
  print(d[n-1])
  
  
  
BellmanFord(n,0,es)