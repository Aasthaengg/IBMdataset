n,m=map(int,input().split())
B=[]
for _ in range(m):
  a,b=map(int,input().split())
  B.append([a-1,b-1])
  
B=sorted(B,key=lambda x:x[1])
ans=m
for i in range(1,m):
  if B[i][0]<B[i-1][1]:
    ans-=1
    B[i][1]=B[i-1][1]
    
print(ans)