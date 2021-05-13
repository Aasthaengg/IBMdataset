from heapq import*

x,y,z,K=map(int,input().split())
a=sorted(list(map(int,input().split())))[::-1]
b=sorted(list(map(int,input().split())))[::-1]
c=sorted(list(map(int,input().split())))[::-1]

h=[]
se=set((0,0,0))
#ans=[]
heappush(h,(-a[0]-b[0]-c[0],0,0,0))

for _ in range(K):
#  print(h)
  
  
  
  tmp,xx,yy,zz=heappop(h)
  print(-tmp)
  for i in range(2):
    for j in range(2):
      for k in range(2):
        if i+j+k==1:
          xn,yn,zn=xx+i,yy+j,zz+k
          if xn>=x:continue
          if yn>=y:continue
          if zn>=z:continue
          if (xn,yn,zn) in se:
            continue 
          heappush(h,(-a[xn]-b[yn]-c[zn],xn,yn,zn))
          se.add((xn,yn,zn))
