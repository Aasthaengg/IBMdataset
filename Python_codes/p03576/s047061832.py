n,k=map(int,input().split())

dot=[]
xxx=[]
yyy=[]

ans=float('inf')

for i in range(n):
  x,y=map(int,input().split())
  dot.append([x,y])
  xxx.append(x)
  yyy.append(y)

xxx.sort()
yyy.sort()

for sx in range(n):
  for sy in range(n):
    for gx in range(sx+1,n):
      for gy in range(sy+1,n):
        cnt=0
        for lst in dot:
          if xxx[sx]<=lst[0]<=xxx[gx]:
            if yyy[sy]<=lst[1]<=yyy[gy]:
              cnt+=1
      
        if cnt>=k:
          if xxx[sx]==xxx[gx] or yyy[sy]==yyy[gy]:
            continue
          ans=min(ans,(xxx[gx]-xxx[sx])*(yyy[gy]-yyy[sy]))


print(ans)