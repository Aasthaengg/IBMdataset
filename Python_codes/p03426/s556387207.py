h,w,d=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(h)]
q=int(input())
LR=[list(map(int,input().split())) for _ in range(q)]
size=h*w+1

B=[[] for _ in range(size)]
for i in range(h):
    for j in range(w):
        B[A[i][j]]=[i,j]

DP=[0]*size
for i in range(d+1,size):
    x,y=B[i]
    z,w=B[i-d]
    DP[i]=DP[i-d]+abs(x-z)+abs(y-w)

for l,r in LR:
    print(DP[r]-DP[l])