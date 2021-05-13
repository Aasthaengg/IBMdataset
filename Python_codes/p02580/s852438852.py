h,w,m=map(int,input().split())
A=[0]*h ; B=[0]*w ;G=[]
for i in range(m):
    x,y=map(int,input().split())
    A[x-1]+=1 ; B[y-1]+=1
    G.append([x-1,y-1])

q=max(A) ; e=max(B)
Q=[i for i in range(h) if A[i]==q] 
W=[j for j in range(w) if B[j]==e];#print(A,B,Q,W)
cnt=len(Q)*len(W)



for i in range(m):
    x,y=G[i]
    if A[x]==q and B[y]==e:
        cnt-=1
#print(grid)
if cnt==0:
    print(q+e-1)
else:
    print(q+e)
