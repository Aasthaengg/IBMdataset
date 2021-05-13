H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))
A_dic={i+1:A[i] for i in range(N)}
Squares=[[0 for i in range(W)] for j in range(H)]

step_w=1
w,h,cnt=0,0,0
for k,v in A_dic.items():
    for i in range(v):
        cnt+=1
        Squares[h][w]=str(k)
        if cnt%W==0:
            h+=1
            step_w*=(-1)
        else:
            w+=step_w

for l in Squares:
    print(' '.join(l))
