N,H,W = map(int,input().split())
A=[0]*N
B=[0]*N

cnt=0
for i in range(N):
  A[i],B[i]=map(int,input().split())
  if A[i]>=H and B[i]>=W:
    cnt +=1
    
print(cnt)