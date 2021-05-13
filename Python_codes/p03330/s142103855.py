# coding: utf-8
# Your code here!
N,C=map(int,input().split())

D=[]
for _ in range(C):
    D.append(list(map(int,input().split())))
    
c=[]
for _ in range(N):
    c.append(list(map(int,input().split())))


col=[[0]*30 for i in range(3)]

for i in range(N):
    for j in range(N):
        col[(i+j+2)%3][c[i][j]-1]+=1

ans=10**9
for col0 in range(C):
    temp0=0
    for i in range(C):
        temp0+=col[0][i]*D[i][col0] 
    for col1 in range(C):
        if col0==col1:
            continue
        #print(temp0)
        temp1=temp0
        for i in range(C):
            temp1+=col[1][i]*D[i][col1]
        for col2 in range(C):
            if col2==col0 or col2==col1:
                continue
            temp2=temp1
            for i in range(C):
                #print(col0,col1,col2)
                temp2+=col[2][i]*D[i][col2]
            #print(col0,col1,col2)
            ans=min(ans,temp2)
            
print(ans)

