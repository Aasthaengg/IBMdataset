N,W=map(int,input().split())
w1,v=map(int,input().split())
if w1>W:
    print(0)
    exit()
lst=[[-1]*(3*N-2) for _ in range(N)]
lst[0][0]=v
for i in range(N-1):
    w,v=map(int,input().split())
    for j in range(N-1,-1,-1):
        for k in range(3*N-2):
            if lst[j][k]!=-1:
                if (j+1)*w1+k+w<=W:
                    lst[j+1][k+w-w1]=max(lst[j][k]+v,lst[j+1][k+w-w1])
    lst[0][w-w1]=max(v,lst[0][w-w1])

lst=[i for j in lst for i in j]
print(max(lst))