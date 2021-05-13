N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

E=[]
color=["white" for _ in range(N)]
for i in range(N):
    if color[i]=="white":
        index,F=i,[]
        while 1:
            if color[index]=="white":
                color[index]="black"
                index=P[index]-1
                F.append(C[index])
            else:break
        E.append(F)

ans=-float("inf")
for A in E:
    length=len(A)
    if sum(A)<0:
        A=A*2
        for i in range(length):
            point=0
            for j in range(min(K,length)):
                point +=A[i+j]
                ans=max(ans,point)
    else:
        div,mod=divmod(K,length)
        base=(div-1)*sum(A)
        A=A*3
        for i in range(length):
            point=0
            for j in range(mod+length):
                point +=A[i+j]
                ans=max(ans,base+point)
print(ans)