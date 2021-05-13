H,W,K=map(int,input().split())
ls=[]
for i in range(H):
    ls.append(input())
ld=[]
#f=0
f=-1
#n=1
ns=0
for i in range(H):
    nstmp=0
    ld.append([])
    for j in range(W):
        if ls[i][j]=="#":
            nstmp+=1
            ns+=1
            if nstmp==2:
                #ld[i].append(j)
                #n+=1
                #ld[i].append((j,ns))
                ld[i].append((j,ns-1))#jより小さいところはns-1区画
                nstmp=1
                #n+=1
    #print("j",j)
    if nstmp==1:
        ld[i].append((j+1,ns))
    if not ld[i]:
        if i==0:
            f=0
        elif not ld[i-1]:
            f+=1
        else:
            ld[i]=ld[i-1]
    #n+=1
#if f==1:
    #ld[0]=ld[1]
if f>-1:
    for i in range(f,-1,-1):
        ld[i]=ld[i+1]
#print(ld)
for i in range(H):
    k=0
    for j in range(W):
        if j<ld[i][k][0]:
            print(ld[i][k][1],end=" ")
        else:
            k+=1
            print(ld[i][k][1],end=" ")
    print("")
