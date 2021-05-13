r,g,b,m=map(int,input().split())

cnt=0
for i in range(0,m+1,r):
  for j in range(0,m+1,g):
      if i+j > m:
        break
      elif (m-(i+j))%b==0:
        cnt+=1
      
print(cnt)