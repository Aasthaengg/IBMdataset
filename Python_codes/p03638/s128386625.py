H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))

c=[[0 for i in range(W)]for j in range(H)]
for k in range(N):
    count=0
    flag=True
    for i in range(H):
        for j in range(W):
            if i%2==0:
                if c[i][j]==0:
                    if count!=a[k]:
                        c[i][j]=k+1
                        count+=1
                    else:
                        flag=False
                        break
            else:
                if c[i][W-1-j]==0:
                    if count!=a[k]:
                        c[i][W-1-j]=k+1
                        count+=1
                    else:
                        flag=False
                        break
        if not flag:
            break
for i in range(H):
    print(*c[i])