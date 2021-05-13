h,w=map(int,input().split())
C=[list(input()) for i in range(h)]
import copy
D=copy.deepcopy(C)
for i in range(h):
    for j in range(w):
        cnt=0
        if C[i][j]=="#":
            D[i][j]="#"
        else:
            if i>0 and j>0 and  C[i-1][j-1]=="#":
                cnt+=1
            if i>0 and  C[i-1][j]=="#":
                cnt+=1
            if i>0 and j<w-1 and C[i-1][j+1]=="#":
                cnt+=1
            if j>0  and C[i][j-1]=="#":
                cnt+=1
            if j<w-1 and C[i][j+1]=="#":
                cnt+=1
            if i<h-1 and j>0 and  C[i+1][j-1]=="#":
                cnt+=1
            if i<h-1 and  C[i+1][j]=="#":
                cnt+=1
            if i<h-1 and j<w-1 and  C[i+1][j+1]=="#":
                cnt+=1
            D[i][j]=str(cnt)
for k in range(h):
    mojiretu = ''.join(D[k])
    print(mojiretu)